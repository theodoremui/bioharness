"""A4 (proposal 06): the cumulative tail-harm guarantee.

Rule. At round t the loop has parent h_t and a candidate h' = h_t + edit. Accept only if the
estimated majority gain is positive and a one-sided test rejects
    H0_t: H(h') >= M,   H(h) = population mean tail loss of h minus that of the seed h_0,
at level alpha_t with sum_t alpha_t <= alpha. Claim: P(some accepted parent has H > M) <= alpha,
provided each test is valid at level alpha_t conditional on everything that produced the candidate.

Model. Tail person i's loss change from edit e is h_e + u_ie, with u_ie iid noise (sd sigma_u) that
is independent across edits and people. A harness's per-person cumulative harm is the sum over the
edits in its lineage, so its noise sd grows like sqrt(#edits). Edits: majority gain a ~ N(0.2, 0.1^2),
tail harm h ~ N(0.1, 0.1^2) (the loop is pushed toward the margin), sigma_u = 0.25, M = 0.5, T = 50,
alpha = 0.05, alpha_t = alpha / T, n_A = 140 majority people.

Gate modes
  none      : majority-only rule (accept if a_hat > 0)
  stepwise  : per-step non-inferiority against the current parent, margin M, level alpha each (bio-creep)
  fresh     : cumulative test against h_0 on n_B new tail people every round (assumption holds)
  fixed     : cumulative test against h_0 on the same n_B tail people every round (reuse)
  cert_seq  : run the majority-only loop, then certify checkpoints h_1..h_T on n_B sealed tail people by
              fixed-sequence testing at level alpha in generation order; deploy the last checkpoint of the
              passing prefix (h_0 if h_1 fails)
  cert_bonf : same, but test every checkpoint at alpha / T and deploy the latest one that passes
Noise: normal, Student t with 3 df (scaled to sd sigma_u), right-skewed mixture (with prob 0.1 a person
is hurt by +3 units, otherwise -1/3; standardized to sd sigma_u), centered lognormal(0, 1) scaled to sigma_u.

Also: the one-sample t-test's realized level at n = 5, 10, 20 under each noise law.

Run: uv run --no-project --with scipy==1.13.1 --with numpy==1.26.4 python a4_guarantee.py
"""
import json
import numpy as np
from scipy.stats import t as tdist

ALPHA, T, M, SIGMA_U = 0.05, 50, 0.5, 0.25
MU_A, SD_A, MU_H, SD_H = 0.2, 0.1, 0.1, 0.1
N_A = 140


def noise(rng, dist, shape):
    if dist == "normal":
        z = rng.standard_normal(shape)
    elif dist == "t3":
        z = rng.standard_t(3, shape) / np.sqrt(3.0)
    elif dist == "skew_mix":
        z = np.where(rng.random(shape) < 0.1, 3.0, -1.0 / 3.0) / 1.0  # mean 0, var = 0.1*9 + 0.9/9 = 1.0
    elif dist == "lognormal":
        x = rng.lognormal(0.0, 1.0, shape)
        z = (x - np.exp(0.5)) / np.sqrt((np.e - 1) * np.e)
    else:
        raise ValueError(dist)
    return SIGMA_U * z


def lower_test_reject(D, margin, level):
    """Reject H0: mean(D) >= margin when the one-sided t statistic is below -t_{n-1, 1-level}."""
    n = D.shape[-1]
    m = D.mean(-1)
    s = D.std(-1, ddof=1)
    crit = tdist.ppf(1 - level, n - 1)
    return (m - margin) / (s / np.sqrt(n)) < -crit


def run_loop(rng, mode, nB, dist, R, schedule="bonf", mu_h=MU_H):
    H = np.zeros(R)                 # true cumulative harm of the parent
    G = np.zeros(R)                 # true cumulative majority gain of the parent
    k = np.zeros(R, dtype=int)      # number of edits in the parent's lineage
    D_fixed = np.zeros((R, nB))     # per-person cumulative harm of the parent on the fixed people
    ever_bad = np.zeros(R, dtype=bool)
    n_acc = np.zeros(R)
    # for certification: record per-checkpoint true H, G and sealed-sample cumulative harm
    ckH, ckG, ckD = [], [], []
    D_sealed = np.zeros((R, nB))
    F = int(mode[6:]) if mode.startswith("retire") else 1
    fold = np.zeros(R, dtype=int)
    for t in range(1, T + 1):
        a = MU_A + SD_A * rng.standard_normal(R)
        h = mu_h + SD_H * rng.standard_normal(R)
        a_hat = a + rng.standard_normal(R) / np.sqrt(N_A)
        maj_ok = a_hat > 0
        level = ALPHA / T if schedule == "bonf" else ALPHA * 6 / (np.pi ** 2 * t ** 2)
        if mode in ("none", "cert_seq", "cert_bonf"):
            gate = np.ones(R, dtype=bool)
        elif mode == "stepwise":
            d_step = h[:, None] + noise(rng, dist, (R, nB))
            gate = lower_test_reject(d_step, M, ALPHA)
        elif mode == "fresh":
            kmax = int(k.max()) + 1
            u = noise(rng, dist, (R, nB, kmax))
            mask = (np.arange(kmax)[None, :] < (k + 1)[:, None])[:, None, :]
            D_c = (H + h)[:, None] + (u * mask).sum(-1)
            gate = lower_test_reject(D_c, M, level)
        elif mode == "fixed":
            D_c = D_fixed + h[:, None] + noise(rng, dist, (R, nB))
            gate = lower_test_reject(D_c, M, level)
        elif mode == "oracle":
            gate = H + h <= M
        elif mode.startswith("retire"):
            # folds of nB / F people; a fold is retired once it certifies an acceptance
            m = nB // F
            D_c = D_fixed + h[:, None] + noise(rng, dist, (R, nB))
            Dc_f = D_c[:, : m * F].reshape(R, F, m)
            sel = np.take_along_axis(Dc_f, np.minimum(fold, F - 1)[:, None, None], axis=1)[:, 0, :]
            gate = lower_test_reject(sel, M, level) & (fold < F)
        acc = maj_ok & gate
        if mode.startswith("retire"):
            fold = fold + acc
        if mode == "fixed" or mode.startswith("retire"):
            D_fixed = np.where(acc[:, None], D_c, D_fixed)
        if mode in ("cert_seq", "cert_bonf"):
            D_sealed = np.where(acc[:, None], D_sealed + h[:, None] + noise(rng, dist, (R, nB)), D_sealed)
        H = np.where(acc, H + h, H)
        G = np.where(acc, G + a, G)
        k = k + acc
        n_acc += acc
        ever_bad |= H > M
        if mode in ("cert_seq", "cert_bonf"):
            ckH.append(H.copy())
            ckG.append(G.copy())
            ckD.append(D_sealed.copy())
    if mode in ("cert_seq", "cert_bonf"):
        ckH = np.array(ckH)          # (T, R)
        ckG = np.array(ckG)
        ckD = np.array(ckD)          # (T, R, nB)
        # a checkpoint identical to h_0 (no edits yet) has D = 0 with zero variance: treat as passing
        nz = ckD.std(-1, ddof=1) > 0
        lvl = ALPHA if mode == "cert_seq" else ALPHA / T
        rej = np.where(nz, lower_test_reject(ckD, M, lvl), True)
        if mode == "cert_seq":
            prefix = np.cumprod(rej, axis=0).astype(bool)          # passing prefix in generation order
            last = np.where(prefix.any(0), T - 1 - np.argmax(prefix[::-1], axis=0), -1)
        else:
            last = np.where(rej.any(0), T - 1 - np.argmax(rej[::-1], axis=0), -1)
        idx = np.arange(R)
        depH = np.where(last >= 0, ckH[np.maximum(last, 0), idx], 0.0)
        depG = np.where(last >= 0, ckG[np.maximum(last, 0), idx], 0.0)
        return dict(err=float((depH > M).mean()), final_H=float(depH.mean()), final_G=float(depG.mean()),
                    accepted=float(n_acc.mean()), deployed_seed=float((depG == 0).mean()))
    return dict(err=float(ever_bad.mean()), final_H=float(H.mean()), final_G=float(G.mean()),
                accepted=float(n_acc.mean()), deployed_seed=float((G == 0).mean()))


def level_check(rng, reps=400_000):
    out = []
    for dist in ["normal", "t3", "skew_mix", "lognormal"]:
        for n in [5, 10, 20]:
            D = M + noise(rng, dist, (reps, n))      # H0 boundary: true mean exactly M
            row = dict(dist=dist, n=n)
            for lvl in [0.05, 0.01, 0.001]:
                row[f"level_{lvl}"] = float(lower_test_reject(D, M, lvl).mean())
            out.append(row)
    return out


@np.errstate(divide="ignore", invalid="ignore")
def main():
    rng = np.random.default_rng(424242)
    print("Realized level of the one-sided t test (reject 'mean harm >= M') at the null boundary")
    lv = level_check(rng)
    for r in lv:
        print(f"  {r['dist']:9s} n={r['n']:2d}: nominal 0.05 -> {r['level_0.05']:.4f}, 0.01 -> {r['level_0.01']:.4f}, "
              f"0.001 -> {r['level_0.001']:.5f}")
    R = 20_000
    rows = []
    print(f"\nLoop: T={T}, M={M}, alpha={ALPHA}, alpha_t=alpha/T, sigma_u={SIGMA_U}, per-edit harm N({MU_H},{SD_H}^2), R={R}")
    print("  dist      nB mode       P(H>M ever or deployed)  mean final H  mean final G  accepted  seed deployed")
    for dist in ["normal", "t3", "skew_mix", "lognormal"]:
        for nB in [5, 10, 20]:
            for mode in ["none", "stepwise", "fresh", "fixed", "cert_seq", "cert_bonf"]:
                if dist != "normal" and mode in ("none", "stepwise"):
                    continue
                r = run_loop(rng, mode, nB, dist, R)
                r.update(dist=dist, nB=nB, mode=mode)
                rows.append(r)
                print(f"  {dist:9s} {nB:2d} {mode:10s} {r['err']:.4f}                  {r['final_H']:+.3f}        "
                      f"{r['final_G']:.3f}        {r['accepted']:.2f}     {r['deployed_seed']:.3f}")
    # price of protection against an oracle that knows the true cumulative harm, and valid fold retirement
    print("\nPrice and fold retirement, normal noise (mu_h = per-edit mean tail harm):")
    extra = []
    for mu_h in [0.1, 0.0]:
        for nB in [5, 10, 20]:
            for mode in ["none", "oracle", "fresh", "fixed", "retire2", "retire4", "cert_seq"]:
                if mode == "retire4" and nB < 8:
                    continue
                r = run_loop(rng, mode, nB, "normal", R, mu_h=mu_h)
                r.update(dist="normal", nB=nB, mode=mode, mu_h=mu_h)
                extra.append(r)
                print(f"  mu_h={mu_h:.1f} nB={nB:2d} {mode:8s}: P(H>M) = {r['err']:.4f}, final H = {r['final_H']:+.3f}, "
                      f"final G = {r['final_G']:.3f}, accepted = {r['accepted']:.2f}")
    for dist in ["skew_mix", "lognormal"]:
        for nB in [10, 20]:
            for mode in ["retire2"]:
                r = run_loop(rng, mode, nB, dist, R)
                r.update(dist=dist, nB=nB, mode=mode, mu_h=MU_H)
                extra.append(r)
                print(f"  {dist} nB={nB:2d} {mode}: P(H>M) = {r['err']:.4f}, final G = {r['final_G']:.3f}")
    # sensitivity: alpha_t = alpha * 6 / (pi^2 t^2) instead of alpha / T
    print("\nalpha-spending schedule alpha_t = 6 alpha / (pi^2 t^2), normal noise:")
    sched = []
    for nB in [5, 10, 20]:
        for mode in ["fresh", "fixed"]:
            r = run_loop(rng, mode, nB, "normal", R, schedule="pi2")
            r.update(dist="normal", nB=nB, mode=mode, schedule="pi2")
            sched.append(r)
            print(f"  nB={nB:2d} {mode:6s}: P(H>M) = {r['err']:.4f}, final G = {r['final_G']:.3f}, accepted = {r['accepted']:.2f}")
    with open(__file__.replace(".py", "_results.json"), "w") as f:
        json.dump(dict(level_check=lv, loop=rows, price_and_retire=extra, schedule_pi2=sched), f, indent=1)


if __name__ == "__main__":
    main()
