"""C (proposal 05): power for the single-edit success profile and for loop-level validation.

Part 1. Two arms (structural variants), single-edit success probability p1 vs p2. Unclustered
sample size, the design effect for edits clustered by proposer seed, and Monte Carlo power with
  logit p_{base, arm, seed} = logit p_arm + u_base + v_{base, arm} + w_seed,
  u ~ N(0, 0.5^2) (base harness), v ~ N(0, tau_int^2) (base x arm heterogeneity), w ~ N(0, sigma_w^2) (seed),
three base harnesses, S seeds per (base, arm), m edits per seed, N = 3 S m edits per arm.
Analyses: (i) conditional on the three bases: cluster-level proportions, arm effect within base,
pooled within-cell variance, t test with 6S - 6 df... (implemented as a two-way fixed-effects contrast);
(ii) generalizing to new base harnesses: base-level differences (3 values), t test with 2 df.

Part 2. Loop-level validation.
 (a) Minimum detectable effect for comparing final held-out improvement between arms, in units of the
     seed-to-seed sd, for paired-by-base designs and for the 2^(4-1) factorial.
 (b) Predictive validation across configurations: power to detect corr(profile, loop outcome) > 0 and to
     show the profile beats parent score (Williams' test for dependent correlations), with measurement
     error in both the profile (finite edits) and the loop outcome (finite seeds).

Run: uv run --no-project --with scipy==1.13.1 --with numpy==1.26.4 python c_power.py
"""
import json
import numpy as np
from scipy.stats import norm, t as tdist
from scipy.special import expit, logit


def n_two_prop(p1, p2, alpha=0.05, power=0.8):
    za, zb = norm.ppf(1 - alpha / 2), norm.ppf(power)
    pb = (p1 + p2) / 2
    return (za * np.sqrt(2 * pb * (1 - pb)) + zb * np.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2 / (p1 - p2) ** 2


def mc_power(rng, p1, p2, S, m, sigma_w, tau_int, reps=2000, alpha=0.05, B=3):
    rej_cond = 0
    rej_pop = 0
    for _ in range(reps):
        u = 0.5 * rng.standard_normal(B)
        props = np.zeros((B, 2, S))
        for arm, p in enumerate([p1, p2]):
            v = tau_int * rng.standard_normal(B)
            w = sigma_w * rng.standard_normal((B, S))
            pr = expit(logit(p) + u[:, None] + v[:, None] + w)
            props[:, arm, :] = rng.binomial(m, pr) / m
        cell_means = props.mean(-1)                   # (B, 2)
        diff_b = cell_means[:, 1] - cell_means[:, 0]
        est = diff_b.mean()
        # (i) conditional on bases: pooled within-cell variance of seed-level proportions
        resid = props - cell_means[..., None]
        df = B * 2 * (S - 1)
        s2 = (resid ** 2).sum() / df
        se = np.sqrt(s2 * 2 / S / B)
        if se > 0 and abs(est / se) > tdist.ppf(1 - alpha / 2, df):
            rej_cond += 1
        # (ii) new bases: t test on the three base-level differences
        sd_b = diff_b.std(ddof=1)
        if sd_b > 0 and abs(est / (sd_b / np.sqrt(B))) > tdist.ppf(1 - alpha / 2, B - 1):
            rej_pop += 1
    return rej_cond / reps, rej_pop / reps


def williams_t(r12, r13, r23, n):
    """Williams' t for H0: corr(1,2) = corr(1,3), variable 1 shared. df = n - 3."""
    detR = 1 - r12 ** 2 - r13 ** 2 - r23 ** 2 + 2 * r12 * r13 * r23
    rbar = (r12 + r13) / 2
    num = (r12 - r13) * np.sqrt((n - 1) * (1 + r23))
    den = np.sqrt(2 * (n - 1) / (n - 3) * detR + rbar ** 2 * (1 - r23) ** 3)
    return num / den


def loop_validation(rng, n_conf, r_profile, r_parent, rel_y, rel_x, reps=20000, alpha=0.05):
    det_profile = 0
    beats = 0
    for _ in range(reps):
        y_true = rng.standard_normal(n_conf)
        x1_true = r_profile * y_true + np.sqrt(1 - r_profile ** 2) * rng.standard_normal(n_conf)
        x2_true = r_parent * y_true + np.sqrt(1 - r_parent ** 2) * rng.standard_normal(n_conf)
        # measurement error: reliabilities rel_y (loop outcome averaged over seeds) and rel_x (profile from finite edits)
        y = y_true + np.sqrt(1 / rel_y - 1) * rng.standard_normal(n_conf)
        x1 = x1_true + np.sqrt(1 / rel_x - 1) * rng.standard_normal(n_conf)
        x2 = x2_true + np.sqrt(1 / rel_x - 1) * rng.standard_normal(n_conf)
        c = np.corrcoef(np.vstack([y, x1, x2]))
        r1, r2, r12 = c[0, 1], c[0, 2], c[1, 2]
        z = np.arctanh(r1) * np.sqrt(n_conf - 3)
        if z > norm.ppf(1 - alpha):          # one-sided: profile predicts the loop outcome
            det_profile += 1
        if williams_t(r1, r2, r12, n_conf) > tdist.ppf(1 - alpha, n_conf - 3):
            beats += 1
    return det_profile / reps, beats / reps


def main():
    rng = np.random.default_rng(505)
    out = {}
    print("Part 1a: edits per arm, unclustered, two-sided alpha = 0.05")
    tab = []
    for p2 in [0.12, 0.15, 0.20]:
        n80, n90 = n_two_prop(0.10, p2, power=0.8), n_two_prop(0.10, p2, power=0.9)
        tab.append(dict(p1=0.10, p2=p2, n80=float(np.ceil(n80)), n90=float(np.ceil(n90))))
        print(f"  0.10 vs {p2:.2f}: {np.ceil(n80):.0f} per arm (80% power), {np.ceil(n90):.0f} (90%)")
    out["unclustered"] = tab
    print("\nPart 1b: design effect 1 + (m - 1) ICC, edits per arm for 0.10 vs 0.15 at 80% power")
    n0 = np.ceil(n_two_prop(0.10, 0.15))
    de = []
    for icc in [0.01, 0.02, 0.05, 0.10]:
        row = {"icc": icc}
        for m in [10, 25, 50]:
            row[f"m{m}"] = float(np.ceil(n0 * (1 + (m - 1) * icc)))
        de.append(row)
        print(f"  ICC {icc:.2f}: m=10 -> {row['m10']:.0f}, m=25 -> {row['m25']:.0f}, m=50 -> {row['m50']:.0f}")
    out["design_effect"] = de
    print("\nPart 1c: Monte Carlo power, 0.10 vs 0.15, 3 base harnesses paired across arms")
    print("  N/arm  m   seeds/base  sigma_w  tau_int | power (i) these bases | power (ii) new bases")
    mcrows = []
    for N in [300, 690, 1200, 2400]:
        for m in [10, 50]:
            S = max(2, int(round(N / (3 * m))))
            for sigma_w in [0.0, 0.3, 0.6]:
                for tau_int in [0.0, 0.2, 0.4]:
                    if tau_int > 0 and sigma_w != 0.3:
                        continue
                    pc, pp = mc_power(rng, 0.10, 0.15, S, m, sigma_w, tau_int)
                    mcrows.append(dict(N=3 * S * m, m=m, S=S, sigma_w=sigma_w, tau_int=tau_int, power_cond=pc, power_pop=pp))
                    print(f"  {3 * S * m:5d} {m:3d}  {S:5d}      {sigma_w:.1f}      {tau_int:.1f}     | {pc:.3f}                 | {pp:.3f}")
    out["mc_power"] = mcrows
    print("\nPart 1d: number of base harnesses needed to generalize to new harnesses (100 edits per base per arm, m = 10, sigma_w = 0.3)")
    nb = []
    for B in [3, 6, 10, 20]:
        for tau_int in [0.0, 0.2, 0.4]:
            pc, pp = mc_power(rng, 0.10, 0.15, 10, 10, 0.3, tau_int, B=B)
            nb.append(dict(B=B, tau_int=tau_int, power_cond=pc, power_pop=pp, N_per_arm=100 * B))
            print(f"  bases {B:2d} (N/arm {100 * B:4d}) tau_int {tau_int:.1f}: power (i) {pc:.3f}, power (ii) {pp:.3f}")
    out["n_bases"] = nb
    # latent-scale ICC implied by sigma_w
    for sw in [0.3, 0.6]:
        print(f"  sigma_w = {sw}: latent ICC = {sw ** 2 / (sw ** 2 + np.pi ** 2 / 3):.3f}")

    print("\nPart 2a: minimum detectable effect (two-sided 0.05, 80% power) in seed-sd units")
    k = norm.ppf(0.975) + norm.ppf(0.8)
    mde = []
    for loops_per_arm in [15, 30, 60]:
        d = k * np.sqrt(2 / loops_per_arm)
        mde.append(dict(loops_per_arm=loops_per_arm, mde=float(d)))
        print(f"  {loops_per_arm} loops per arm (paired by base, base effects cancel): MDE = {d:.2f} sd")
    d_fact = k * np.sqrt(1 / 60 + 1 / 60)
    print(f"  2^(4-1) factorial, 8 cells x 3 bases x 5 seeds = 120 loops: main-effect MDE = {d_fact:.2f} sd")
    out["mde"] = mde
    out["mde_factorial"] = float(d_fact)

    print("\nPart 2b: predictive validation across configurations (one-sided 0.05)")
    print("  n_conf r_profile r_parent rel_y rel_x | P(detect r_profile > 0) | P(profile beats parent score)")
    lv = []
    for n_conf in [24, 48, 96]:
        for r_prof, r_par in [(0.5, 0.0), (0.7, 0.3), (0.6, 0.4)]:
            for rel_y, rel_x in [(0.83, 0.75), (0.5, 0.5)]:
                pd, pb = loop_validation(rng, n_conf, r_prof, r_par, rel_y, rel_x, reps=10000)
                lv.append(dict(n_conf=n_conf, r_profile=r_prof, r_parent=r_par, rel_y=rel_y, rel_x=rel_x,
                               power_detect=pd, power_beats=pb))
                print(f"  {n_conf:5d}  {r_prof:.1f}       {r_par:.1f}      {rel_y:.2f}  {rel_x:.2f} | {pd:.3f}                   | {pb:.3f}")
    out["loop_validation"] = lv
    with open(__file__.replace(".py", "_results.json"), "w") as f:
        json.dump(out, f, indent=1)


if __name__ == "__main__":
    main()
