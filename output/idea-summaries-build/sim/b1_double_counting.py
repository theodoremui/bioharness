"""B1 (proposal 08): context-aware measurement double-counts the referral.

Setting. Class C in {0, 1} (for example high fall risk). Referral H in {0, 1}, P(H = 1) = 1/2, wrong with
probability q: P(C = H | H) = 1 - q, so the decision maker's prior is pi_H = P(C = 1 | H) = 1 - q if H = 1
and q if H = 0. Latent truth T | C ~ N(mu_C, tau^2), mu_0 = 0, mu_1 = Delta. Blind measurement
M_0 = T + e, e ~ N(0, s^2) independent of (T, H). Likelihood calibrated on blind measurements:
f(m | C) = N(mu_C, V), V = tau^2 + s^2. The agent reports M_g = (1 - g) M_0 + g m_H with m_H = mu_H.
The decision maker computes p_g = P(C = 1 | H, M) by Bayes with prior pi_H and likelihood f at M = M_g.

Claims checked.
 (1) Expected log loss of p_g exceeds that of p_0 for every g != 0 (0 < q < 1).
 (2) MSE(g) = E[(M_g - T)^2] = (1 - g)^2 s^2 + g^2 (tau^2 + q Delta^2), minimized at
     g* = s^2 / (s^2 + tau^2 + q Delta^2), with MSE(g) < MSE(0) for all 0 < g < 2 g*.
 (3) logit p_g = logit pi_H + g Delta^2 / (2V) (2H - 1) + (1 - g) LLR(M_0): the report inflates the prior
     log-odds toward the referral and shrinks the weight on evidence.
 Also: penalty split by correct vs wrong referral, error rate at threshold 1/2, and two recalibration
 variants (pooled over H, which still double counts; stratified by H, which removes the penalty for g < 1).

Run: uv run --no-project --with scipy==1.13.1 --with numpy==1.26.4 python b1_double_counting.py
"""
import itertools
import json
import numpy as np
from scipy.stats import norm
from scipy.special import expit


def logloss(p, c):
    p = np.clip(p, 1e-300, 1 - 1e-16)
    return -(c * np.log(p) + (1 - c) * np.log1p(-p))


def setup(Delta, tau, s, q):
    V = tau ** 2 + s ** 2
    return V


def expected_scores(Delta, tau, s, q, g, recal=None, n_grid=40001):
    """Expected log loss, Brier and error rate by quadrature over M_0, using the symmetry H=1 <-> H=0.
    recal: None (blind-calibrated likelihood), 'pooled' (Gaussian fit of M_g | C pooled over H),
    'strat' (Gaussian fit of M_g | C, H)."""
    V = tau ** 2 + s ** 2
    sd = np.sqrt(V)
    grid = np.linspace(-12 * sd + 0, Delta + 12 * sd, n_grid)
    dx = grid[1] - grid[0]
    H = 1
    pi = 1 - q
    mH = Delta
    out = dict(ll=0.0, brier=0.0, err=0.0, ll_right=0.0, ll_wrong=0.0)
    # moments of M_g | C for recalibration (pooled over H, using symmetry: H = C w.p. 1 - q)
    for c, pc in [(1, 1 - q), (0, q)]:
        dens = norm.pdf(grid, loc=Delta * c, scale=sd)
        Mg = (1 - g) * grid + g * mH
        if recal is None:
            llr = (Delta / V) * (Mg - Delta / 2)
        elif recal == "strat":
            # M_g | C, H ~ N((1-g) mu_C + g m_H, (1-g)^2 V): exact for g != 1
            if abs(1 - g) < 1e-12:
                llr = np.zeros_like(grid)
            else:
                v = (1 - g) ** 2 * V
                m1 = (1 - g) * Delta + g * mH
                m0 = g * mH
                llr = norm.logpdf(Mg, m1, np.sqrt(v)) - norm.logpdf(Mg, m0, np.sqrt(v))
        elif recal == "pooled":
            # pooled over H: M_g | C=1 has mean (1-g) Delta + g (Delta (1-q) + 0 q), var (1-g)^2 V + g^2 Delta^2 q (1-q)
            mean1 = (1 - g) * Delta + g * Delta * (1 - q)
            mean0 = g * Delta * q
            var = (1 - g) ** 2 * V + g ** 2 * Delta ** 2 * q * (1 - q)
            llr = norm.logpdf(Mg, mean1, np.sqrt(var)) - norm.logpdf(Mg, mean0, np.sqrt(var))
        p = expit(np.log(pi / (1 - pi)) + llr)
        w = dens * dx * pc
        ll = (logloss(p, c) * w).sum()
        out["ll"] += ll
        out["brier"] += (((p - c) ** 2) * w).sum()
        out["err"] += (((p > 0.5) != c) * w).sum()
        if c == 1:
            out["ll_right"] += ll / (1 - q)       # referral correct (C = H = 1)
        else:
            out["ll_wrong"] += ll / q             # referral wrong (C = 0, H = 1)
    return out


def mc_check(Delta, tau, s, q, g, n, rng):
    Hh = rng.random(n) < 0.5
    wrong = rng.random(n) < q
    C = np.where(wrong, ~Hh, Hh).astype(int)
    T = Delta * C + tau * rng.standard_normal(n)
    M0 = T + s * rng.standard_normal(n)
    mH = Delta * Hh
    Mg = (1 - g) * M0 + g * mH
    V = tau ** 2 + s ** 2
    pi = np.where(Hh, 1 - q, q)
    p = expit(np.log(pi / (1 - pi)) + (Delta / V) * (Mg - Delta / 2))
    return logloss(p, C).mean(), ((Mg - T) ** 2).mean()


def main():
    rng = np.random.default_rng(808)
    tau = 1.0
    rows = []
    strict_viol = 0
    n_strict = 0
    for Delta, s, q in itertools.product([1.0, 2.0, 3.0], [0.5, 1.0, 2.0], [0.1, 0.2, 0.3, 0.5]):
        D = tau ** 2 + q * Delta ** 2
        g_star = s ** 2 / (s ** 2 + D)
        mse0 = s ** 2
        mse_star = s ** 2 * D / (s ** 2 + D)
        base = expected_scores(Delta, tau, s, q, 0.0)
        # strictness on a grid of g including negative and > 1
        for g in [-0.5, -0.05, 0.01, 0.05, 0.1, 0.25, 0.5, 0.75, 1.0, 1.5]:
            n_strict += 1
            if expected_scores(Delta, tau, s, q, g)["ll"] - base["ll"] <= 0:
                strict_viol += 1
        at = expected_scores(Delta, tau, s, q, g_star)
        pooled = expected_scores(Delta, tau, s, q, g_star, recal="pooled")
        strat = expected_scores(Delta, tau, s, q, g_star, recal="strat")
        rows.append(dict(Delta=Delta, s=s, q=q, g_star=g_star, mse_ratio=mse_star / mse0,
                         ll0=base["ll"], ll_star=at["ll"], penalty=at["ll"] - base["ll"],
                         rel_penalty=(at["ll"] - base["ll"]) / base["ll"],
                         penalty_right=at["ll_right"] - base["ll_right"], penalty_wrong=at["ll_wrong"] - base["ll_wrong"],
                         err0=base["err"], err_star=at["err"], brier0=base["brier"], brier_star=at["brier"],
                         penalty_pooled_recal=pooled["ll"] - base["ll"], penalty_strat_recal=strat["ll"] - base["ll"],
                         prior_shift_logodds=g_star * Delta ** 2 / (2 * (tau ** 2 + s ** 2)),
                         evidence_weight=1 - g_star))
    print(f"strictness check: {strict_viol} violations out of {n_strict} (Delta, s, q, g) cells with g != 0")
    print(" Delta  s    q   | g*    MSE(g*)/MSE(0) | logloss(0) penalty(g*) rel   | right / wrong referral | err 0 -> g*   | pooled recal / strat recal")
    for r in rows:
        print(f" {r['Delta']:.0f}    {r['s']:.1f}  {r['q']:.1f}  | {r['g_star']:.3f}  {r['mse_ratio']:.3f}          | {r['ll0']:.4f}     "
              f"{r['penalty']:+.4f}  {r['rel_penalty']:+.1%} | {r['penalty_right']:+.4f} / {r['penalty_wrong']:+.4f}    | "
              f"{r['err0']:.3f} -> {r['err_star']:.3f} | {r['penalty_pooled_recal']:+.4f} / {r['penalty_strat_recal']:+.1e}")
    # Monte Carlo check of quadrature and MSE formula on a few cells
    print("\nMonte Carlo check (2,000,000 cases per cell):")
    mc = []
    for Delta, s, q, g in [(2.0, 1.0, 0.2, 0.357), (1.0, 2.0, 0.3, 0.6), (3.0, 0.5, 0.1, 0.1), (2.0, 1.0, 0.2, 1.0)]:
        ll_q = expected_scores(Delta, tau, s, q, g)["ll"]
        mse_f = (1 - g) ** 2 * s ** 2 + g ** 2 * (tau ** 2 + q * Delta ** 2)
        ll_mc, mse_mc = mc_check(Delta, tau, s, q, g, 2_000_000, rng)
        mc.append(dict(Delta=Delta, s=s, q=q, g=g, ll_quad=ll_q, ll_mc=float(ll_mc), mse_formula=mse_f, mse_mc=float(mse_mc)))
        print(f"  Delta={Delta} s={s} q={q} g={g}: log loss quad {ll_q:.4f} vs MC {ll_mc:.4f}; MSE formula {mse_f:.4f} vs MC {mse_mc:.4f}")
    # worked example curve
    print("\nWorked example Delta = 2 tau, s = tau, q = 0.2: g, MSE, log-loss penalty, error rate")
    curve = []
    base = expected_scores(2.0, tau, 1.0, 0.2, 0.0)
    for g in [0.0, 0.1, 0.2, 0.3, 0.357, 0.5, 0.7, 1.0]:
        sc = expected_scores(2.0, tau, 1.0, 0.2, g)
        mse = (1 - g) ** 2 + g ** 2 * (1 + 0.2 * 4)
        curve.append(dict(g=g, mse=mse, penalty=sc["ll"] - base["ll"], err=sc["err"]))
        print(f"  g={g:.3f}: MSE {mse:.3f}, penalty {sc['ll'] - base['ll']:+.4f} nats, error {sc['err']:.3f}")
    # A decision maker who ignores the referral (flat prior 1/2) gains from context-aware measurement
    print("\nDecision maker who ignores H (flat prior), Delta = 2, s = 1, q = 0.2: log loss by g")
    ign = []
    for g in [0.0, 0.1, 0.2, 0.357, 0.5]:
        tot = 0.0
        V = tau ** 2 + 1.0
        sd = np.sqrt(V)
        grid = np.linspace(-12 * sd, 2.0 + 12 * sd, 40001)
        dx = grid[1] - grid[0]
        for c, pc in [(1, 0.8), (0, 0.2)]:        # H = 1 branch; H = 0 is the mirror image
            dens = norm.pdf(grid, loc=2.0 * c, scale=sd)
            Mg = (1 - g) * grid + g * 2.0
            p = expit((2.0 / V) * (Mg - 1.0))
            tot += (logloss(p, c) * dens * dx * pc).sum()
        ign.append(dict(g=g, ll=float(tot)))
        print(f"  g={g:.3f}: log loss {tot:.4f} (Bayes with prior and blind M: {expected_scores(2.0, tau, 1.0, 0.2, 0.0)['ll']:.4f})")
    with open(__file__.replace(".py", "_results.json"), "w") as f:
        json.dump(dict(strict_violations=strict_viol, n_strict=n_strict, rows=rows, mc=mc, curve=curve,
                       ignores_referral=ign), f, indent=1)


if __name__ == "__main__":
    main()
