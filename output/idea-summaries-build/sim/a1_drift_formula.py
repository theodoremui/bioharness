"""A1 (proposal 06): closed form for E[b | S > 0] under the mean acceptance rule.

Model. Candidate edit has true loss reductions (a, b) jointly Gaussian:
  a ~ N(mu_a, sig_a^2), b ~ N(mu_b, sig_b^2), corr(a, b) = rho.
Estimates a_hat = a + e_a, b_hat = b + e_b with e_a ~ N(0, s_a^2), e_b ~ N(0, s_b^2)
independent of each other and of (a, b). The mean rule accepts if
  S = w a_hat + (1 - w) b_hat > 0.
Claim:
  E[b | S > 0] = mu_b + Cov(b, S) / sig_S * lambda(mu_S / sig_S),  lambda(z) = phi(z) / Phi(z)
  Cov(b, S) = w rho sig_a sig_b + (1 - w) sig_b^2
  mu_S = w mu_a + (1 - w) mu_b
  sig_S^2 = w^2 (sig_a^2 + s_a^2) + (1 - w)^2 (sig_b^2 + s_b^2) + 2 w (1 - w) rho sig_a sig_b

Run: uv run --no-project --with scipy==1.13.1 --with numpy==1.26.4 python a1_drift_formula.py
"""
import itertools
import json
import numpy as np
from scipy.stats import norm


def closed_form(mu_a, mu_b, sig_a, sig_b, rho, s_a, s_b, w):
    cov_bS = w * rho * sig_a * sig_b + (1 - w) * sig_b ** 2
    mu_S = w * mu_a + (1 - w) * mu_b
    var_S = (w ** 2 * (sig_a ** 2 + s_a ** 2) + (1 - w) ** 2 * (sig_b ** 2 + s_b ** 2)
             + 2 * w * (1 - w) * rho * sig_a * sig_b)
    sig_S = np.sqrt(var_S)
    z = mu_S / sig_S
    lam = np.exp(norm.logpdf(z) - norm.logcdf(z))
    return mu_b + cov_bS / sig_S * lam, norm.cdf(z)


def mc(mu_a, mu_b, sig_a, sig_b, rho, s_a, s_b, w, n, rng):
    z1 = rng.standard_normal(n)
    z2 = rng.standard_normal(n)
    a = mu_a + sig_a * z1
    b = mu_b + sig_b * (rho * z1 + np.sqrt(1 - rho ** 2) * z2)
    S = w * (a + s_a * rng.standard_normal(n)) + (1 - w) * (b + s_b * rng.standard_normal(n))
    acc = S > 0
    k = acc.sum()
    if k < 200:
        return np.nan, np.nan, k
    bb = b[acc]
    return bb.mean(), bb.std(ddof=1) / np.sqrt(k), k


def main():
    rng = np.random.default_rng(20261124)
    sig_a = 1.0
    grid = dict(
        rho=[-0.9, -0.6, -0.3, 0.0, 0.3, 0.6, 0.9],
        w=[0.5, 0.8, 0.9, 0.95],
        ratio=[0.5, 1.0, 2.0, 4.0],          # sig_b / sig_a
        noise=[0.0, 0.5, 2.0],               # per-person noise sd sqrt(v) relative to sig_a, with n_A + n_B = 20 people scale
        mus=[(0.0, 0.0), (-0.5, -0.5), (0.3, -0.3), (-1.0, 0.2)],
    )
    n_tot = 20  # s_a^2 = v / n_A, s_b^2 = v / n_B with n_A = w n_tot, n_B = (1 - w) n_tot
    n_draw = 400_000
    rows = []
    for rho, w, ratio, noise, (mu_a, mu_b) in itertools.product(*grid.values()):
        sig_b = ratio * sig_a
        v = (noise * sig_a) ** 2 * n_tot  # so that s_a, s_b are comparable to sig_a when noise = 1
        nA, nB = w * n_tot, (1 - w) * n_tot
        s_a, s_b = np.sqrt(v / nA), np.sqrt(v / nB)
        cf, pacc = closed_form(mu_a, mu_b, sig_a, sig_b, rho, s_a, s_b, w)
        m, se, k = mc(mu_a, mu_b, sig_a, sig_b, rho, s_a, s_b, w, n_draw, rng)
        rows.append(dict(rho=rho, w=w, ratio=ratio, noise=noise, mu_a=mu_a, mu_b=mu_b,
                         cf=float(cf), mc=float(m), se=float(se), k=int(k), p_acc=float(pacc)))
    err = np.array([abs(r["cf"] - r["mc"]) for r in rows if np.isfinite(r["mc"])])
    zs = np.array([abs(r["cf"] - r["mc"]) / r["se"] for r in rows if np.isfinite(r["mc"])])
    rel = np.array([abs(r["cf"] - r["mc"]) / (r["ratio"] * sig_a) for r in rows if np.isfinite(r["mc"])])
    n_cells = len(err)
    print(f"cells checked: {n_cells} of {len(rows)} (cells with fewer than 200 acceptances skipped)")
    print(f"draws per cell: {n_draw}")
    print(f"max |closed form - MC|            = {err.max():.4f} (units of sig_a = 1)")
    print(f"max |error| / sig_b               = {rel.max():.4f}")
    print(f"max |error| / MC standard error   = {zs.max():.2f}; mean = {zs.mean():.2f}; share > 3: {(zs > 3).mean():.4f}")
    # Expected |z| for a correct formula is about 0.80 and the max over ~1300 cells is about 3.3 to 3.8.

    # Sign condition check: when mu_b <= 0 and rho < -(1 - w) sig_b / (w sig_a), E[b | S > 0] < 0.
    viol = 0
    nsuff = 0
    neg_but_not_suff = 0
    for r in rows:
        thr = -(1 - r["w"]) * r["ratio"] / r["w"]
        suff = (r["mu_b"] <= 0) and (r["rho"] < thr)
        if suff:
            nsuff += 1
            if r["cf"] >= 0:
                viol += 1
        elif r["cf"] < 0:
            neg_but_not_suff += 1
    print(f"sufficient condition cells: {nsuff}, violations: {viol}")
    print(f"cells with negative tail drift that the sufficient condition misses: {neg_but_not_suff}")

    # Worked StaBLE-like example: n_A = 140, n_B = 20, sig_b = sig_a.
    w = 140 / 160
    print(f"threshold rho* for w = {w:.3f}, sig_b/sig_a = 1: {-(1 - w) / w:.4f}")
    for ratio in [0.5, 1, 2, 4]:
        print(f"  sig_b/sig_a = {ratio}: rho* = {-(1 - w) * ratio / w:.3f}")

    with open(__file__.replace(".py", "_results.json"), "w") as f:
        json.dump(dict(n_cells=n_cells, max_abs_err=float(err.max()), max_z=float(zs.max()),
                       mean_z=float(zs.mean()), rows=rows), f, indent=1)


if __name__ == "__main__":
    main()
