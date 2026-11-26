"""A2 (proposal 06): best-of-K selection (winner's curse) and the tail.

Each round proposes K independent candidates with (a_k, b_k, S_k) as in A1. The loop picks
k* = argmax_k S_k and accepts if S_{k*} > 0.

Exact result (derived in theory-checks.md). Because candidates are independent and
E[b_k | S_1..S_K] = mu_b + beta (S_k - mu_S) with beta = Cov(b, S) / sig_S^2,
  E[b_{k*} | S_(K) > 0] = mu_b + Cov(b, S) / sig_S * m_K(c),   c = -mu_S / sig_S,
  m_K(c) = E[Z_(K) | Z_(K) > c] = int_c^inf z K phi(z) Phi(z)^(K-1) dz / (1 - Phi(c)^K),
where Z_(K) is the max of K iid standard normals. K = 1 gives lambda(mu_S / sig_S).
Approximation: Z_(K) ~ N(e_K, v_K) with Blom e_K = Phi^-1((K - 0.375) / (K + 0.25)), then
  m_K(c) ~ e_K + sqrt(v_K) * lambda((e_K - c) / sqrt(v_K)).
v_K is taken from quadrature (a closed approximation for v_K is noted in the report).

Run: uv run --no-project --with scipy==1.13.1 --with numpy==1.26.4 python a2_best_of_k.py
"""
import itertools
import json
import numpy as np
from scipy.stats import norm
from scipy.integrate import quad


def m_exact(K, c):
    num = quad(lambda z: z * K * norm.pdf(z) * norm.cdf(z) ** (K - 1), c, np.inf, limit=200)[0]
    den = 1 - norm.cdf(c) ** K
    return num / den


def moments_max(K):
    e = quad(lambda z: z * K * norm.pdf(z) * norm.cdf(z) ** (K - 1), -np.inf, np.inf, limit=200)[0]
    e2 = quad(lambda z: z * z * K * norm.pdf(z) * norm.cdf(z) ** (K - 1), -np.inf, np.inf, limit=200)[0]
    return e, e2 - e * e


def m_approx(K, c, vK):
    eK = norm.ppf((K - 0.375) / (K + 0.25)) if K > 1 else 0.0
    sd = np.sqrt(vK)
    z = (eK - c) / sd
    return eK + sd * np.exp(norm.logpdf(z) - norm.logcdf(z))


def params(mu_a, mu_b, sig_a, sig_b, rho, s_a, s_b, w):
    cov_bS = w * rho * sig_a * sig_b + (1 - w) * sig_b ** 2
    mu_S = w * mu_a + (1 - w) * mu_b
    var_S = (w ** 2 * (sig_a ** 2 + s_a ** 2) + (1 - w) ** 2 * (sig_b ** 2 + s_b ** 2)
             + 2 * w * (1 - w) * rho * sig_a * sig_b)
    return cov_bS, mu_S, np.sqrt(var_S)


def mc(K, mu_a, mu_b, sig_a, sig_b, rho, s_a, s_b, w, n_rounds, rng):
    z1 = rng.standard_normal((n_rounds, K))
    z2 = rng.standard_normal((n_rounds, K))
    a = mu_a + sig_a * z1
    b = mu_b + sig_b * (rho * z1 + np.sqrt(1 - rho ** 2) * z2)
    S = w * (a + s_a * rng.standard_normal((n_rounds, K))) + (1 - w) * (b + s_b * rng.standard_normal((n_rounds, K)))
    k = S.argmax(axis=1)
    Smax = S[np.arange(n_rounds), k]
    bsel = b[np.arange(n_rounds), k]
    acc = Smax > 0
    bb = bsel[acc]
    return bb.mean(), bb.std(ddof=1) / np.sqrt(acc.sum()), acc.mean()


def main():
    rng = np.random.default_rng(7)
    Ks = [1, 2, 5, 10, 20, 50]
    vK = {K: moments_max(K)[1] for K in Ks}
    eK = {K: moments_max(K)[0] for K in Ks}
    print("K, E[max], Var[max], Blom E[max], sqrt(2 ln K)")
    for K in Ks:
        blom = norm.ppf((K - 0.375) / (K + 0.25)) if K > 1 else 0.0
        print(f"  {K:3d}  {eK[K]:.4f}  {vK[K]:.4f}  {blom:.4f}  {np.sqrt(2*np.log(K)) if K>1 else 0:.4f}")

    rows = []
    sig_a = 1.0
    n_tot = 20
    for K, rho, w, ratio, noise, (mu_a, mu_b) in itertools.product(
            Ks, [-0.8, -0.4, 0.0, 0.4, 0.8], [0.8, 0.9], [1.0, 2.0], [0.0, 1.0],
            [(0.0, 0.0), (-0.5, -0.5), (-1.0, 0.2)]):
        sig_b = ratio
        v = (noise * sig_a) ** 2 * n_tot
        s_a, s_b = np.sqrt(v / (w * n_tot)), np.sqrt(v / ((1 - w) * n_tot))
        cov, muS, sigS = params(mu_a, mu_b, sig_a, sig_b, rho, s_a, s_b, w)
        c = -muS / sigS
        ex = mu_b + cov / sigS * m_exact(K, c)
        ap = mu_b + cov / sigS * m_approx(K, c, vK[K])
        n_rounds = max(400_000 // K, 20_000)
        m, se, pacc = mc(K, mu_a, mu_b, sig_a, sig_b, rho, s_a, s_b, w, n_rounds, rng)
        rows.append(dict(K=K, rho=rho, w=w, ratio=ratio, noise=noise, mu_a=mu_a, mu_b=mu_b,
                         exact=ex, approx=ap, mc=m, se=se, p_acc=pacc,
                         amplification=m_exact(K, c) / m_exact(1, c)))
    z = np.array([abs(r["exact"] - r["mc"]) / r["se"] for r in rows])
    e_ex = np.array([abs(r["exact"] - r["mc"]) for r in rows])
    e_ap = np.array([abs(r["approx"] - r["exact"]) for r in rows])
    print(f"cells: {len(rows)}")
    print(f"exact vs MC: max |err| = {e_ex.max():.4f}, max |z| = {z.max():.2f}, mean |z| = {z.mean():.2f}")
    print(f"approx vs exact: max |err| = {e_ap.max():.4f} (units of sig_a), "
          f"median = {np.median(e_ap):.4f}")
    # amplification factor m_K(c) / m_1(c) at c = -mu_S/sig_S = 0 and c = 1 (strict) and c = -2 (lenient)
    print("winner's-curse amplification of the selection term relative to K = 1, by c = -mu_S / sig_S:")
    for c in [-2.0, -1.0, 0.0, 1.0, 2.0]:
        print("  c = %+.1f: " % c + ", ".join(f"K={K}: {m_exact(K, c) / m_exact(1, c):.2f}" for K in Ks))
    # absolute selection factor m_K(c) and a closed two-regime approximation
    # m_K(c) ~ max(e_K, phi(c) / (1 - Phi(c))): lenient threshold -> mean of the max; strict -> one exceedance
    print("m_K(c) exact | two-regime approx max(Blom e_K, phi(c)/(1-Phi(c))):")
    worst2 = 0.0
    for c in [-2.0, -1.0, -0.5, 0.0, 0.5, 1.0, 2.0]:
        cells = []
        for K in Ks:
            ex_m = m_exact(K, c)
            blom = norm.ppf((K - 0.375) / (K + 0.25)) if K > 1 else -np.inf
            ap2 = max(blom, norm.pdf(c) / norm.sf(c))
            worst2 = max(worst2, abs(ap2 - ex_m))
            cells.append(f"K={K}: {ex_m:.3f}|{ap2:.3f}")
        print("  c = %+.1f: " % c + ", ".join(cells))
    print(f"two-regime approx: max |error| in m_K over this table = {worst2:.3f}")
    # per-round (unconditional) tail change E[b_sel 1{accept}] at c = 0, mu_b = 0, Cov/sig_S = -0.1
    print("per-round tail change with mu_b = 0, Cov/sig_S = -0.1, c = 0:")
    for K in Ks:
        p = 1 - norm.cdf(0.0) ** K
        print(f"  K={K}: P(accept) = {p:.3f}, E[b | accept] = {-0.1 * m_exact(K, 0.0):+.3f}, per round = {-0.1 * m_exact(K, 0.0) * p:+.3f}")
    # sign flip example: Cov(b, S) > 0 with mu_b < 0
    mu_a, mu_b, rho, w, ratio = -1.0, -0.2, 0.3, 0.9, 1.0
    cov, muS, sigS = params(mu_a, mu_b, 1.0, ratio, rho, 0.0, 0.0, w)
    print("Cov(b,S) > 0 with mu_b < 0 (mu_a=-1, mu_b=-0.2, rho=0.3, w=0.9, no noise): larger K helps the tail")
    for K in Ks:
        print(f"  K={K}: E[b_sel | accept] = {mu_b + cov / sigS * m_exact(K, -muS / sigS):+.3f}")
    with open(__file__.replace(".py", "_results.json"), "w") as f:
        json.dump(dict(max_z=float(z.max()), mean_z=float(z.mean()), max_abs_err=float(e_ex.max()),
                       approx_max_err=float(e_ap.max()), rows=rows), f, indent=1)


if __name__ == "__main__":
    main()
