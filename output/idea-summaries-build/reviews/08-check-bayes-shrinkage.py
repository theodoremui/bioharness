# Effective shrinkage of the unrestricted MSE-optimal rule E[T | M0, H] in the Gaussian model of Proposition 1.
import numpy as np
import math
class norm:
    @staticmethod
    def pdf(x, m, sd): return np.exp(-0.5*((x-m)/sd)**2)/(sd*math.sqrt(2*math.pi))
def run(D, s, q, tau=1.0):
    mu = np.array([0.0, D]); V = tau**2 + s**2; k = tau**2 / V
    x = np.linspace(-8, 8 + D, 40001); dx = x[1] - x[0]
    out = {}
    for H in (0, 1):
        pi1 = 1 - q if H == 1 else q
        f0 = norm.pdf(x, mu[0], np.sqrt(V)); f1 = norm.pdf(x, mu[1], np.sqrt(V))
        dens = (1 - pi1) * f0 + pi1 * f1
        p1 = pi1 * f1 / dens
        condmean = (1 - p1) * (mu[0] + k * (x - mu[0])) + p1 * (mu[1] + k * (x - mu[1]))
        out[H] = (x, dens, condmean)
    # framing effect: average over the blind-measurement distribution (pooled over H) of E[T|M0,H=1]-E[T|M0,H=0]
    x, d0, c0 = out[0]; _, d1, c1 = out[1]
    w = 0.5 * (d0 + d1)
    TE = np.sum(w * (c1 - c0)) * dx
    # MSE of the Bayes rule vs best linear fixed blend
    gstar = s**2 / (s**2 + tau**2 + q * D**2)
    return TE / D, gstar
for D, s, q in [(2, 1, 0.2), (1, 1, 0.2), (3, 1, 0.1), (2, 0.5, 0.2), (2, 2, 0.2), (1, 0.5, 0.3)]:
    gb, gs = run(D, s, q)
    print(f"Delta={D} s={s} q={q}: gamma_Bayes(eff)={gb:.3f} gamma*={gs:.3f} diff={gb-gs:+.3f}")

def decision(D, s, q, tau=1.0):
    mu0, mu1 = 0.0, D; V = tau**2 + s**2; k = tau**2 / V
    x = np.linspace(-10, 10 + D, 60001); dx = x[1] - x[0]
    llr = lambda m: (D / V) * (m - D / 2)
    ll0 = llB = mse0 = mseB = 0.0
    for H in (0, 1):
        pi1 = 1 - q if H == 1 else q
        for C, pc in ((1, pi1), (0, 1 - pi1)):
            fx = norm.pdf(x, D if C else 0.0, np.sqrt(V))        # M0 | C
            f0 = norm.pdf(x, 0.0, np.sqrt(V)); f1 = norm.pdf(x, D, np.sqrt(V))
            p1 = pi1 * f1 / (pi1 * f1 + (1 - pi1) * f0)
            mB = (1 - p1) * (k * x) + p1 * (D + k * (x - D))     # E[T | M0, H]
            for m, acc in ((x, 0), (mB, 1)):
                lg = np.log(pi1 / (1 - pi1)) + llr(m)
                p = 1 / (1 + np.exp(-lg))
                ll = -np.log(p if C else 1 - p)
                val = 0.5 * pc * np.sum(fx * ll) * dx
                if acc == 0: ll0 += val
                else: llB += val
            # MSE: E[(m - T)^2 | M0, C] = (m - E[T|M0,C])^2 + Var(T|M0,C)
            ETc = (D if C else 0.0) + k * (x - (D if C else 0.0)); vT = tau**2 * s**2 / V
            mse0 += 0.5 * pc * np.sum(fx * ((x - ETc)**2 + vT)) * dx
            mseB += 0.5 * pc * np.sum(fx * ((mB - ETc)**2 + vT)) * dx
    return ll0, llB, mse0, mseB
for D, s, q in [(2, 1, 0.2), (1, 1, 0.2), (2, 2, 0.2)]:
    ll0, llB, m0, mB = decision(D, s, q)
    print(f"Delta={D} s={s} q={q}: logloss blind {ll0:.3f} Bayes-rule {llB:.3f} (+{llB-ll0:.3f}); MSE ratio {mB/m0:.3f}")
