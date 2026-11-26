"""B2 (proposal 08): path splicing as an interventional estimate of direct and indirect framing effects.

Toy agent, per video v with true value theta_v:
  path phase : given framing F in {a, b} (and optionally a run-level hidden state U), choose a tool path
               P in {0, 1} (1 = trim at the first large excursion); P(P = 1) = expit(beta_F + phi U).
               Reasoning text R is written in this phase and repeats the framing (R = F).
  tools      : O = theta_v + delta P + eta_{v,P}, with eta cached per (video, path).
  report     : M = O + gamma 1[F_rep = a] + iota P 1[F_rep = a] + kappa 1[R in context and R = a]
                 + lam P U_rep + eps.
Natural run: F_rep = F, R = F, U_rep = U (the same run). Splice (f_path -> f_rep): take P, O (and, in the
'carry' variant, R) from a run under f_path and run the report step under f_rep with fresh report noise
and a fresh U_rep (a stateless report call).

Estimands (mediator = tool path): cells mu(f_path, f_rep) = E_v E_{P ~ pi(.|v, f_path)} m(v, f_rep, P),
where m is the report mean when the report step sees framing f_rep and tool path P only.
  TE = mu(b, b) - mu(a, a); IDE_a = mu(a, b) - mu(a, a); IIE_b = mu(b, b) - mu(a, b);
  IIE_a = mu(b, a) - mu(a, a); IDE_b = mu(b, b) - mu(b, a); interaction = mu(b,b) - mu(b,a) - mu(a,b) + mu(a,a).

Variants
  V1 ideal: kappa = 0, iota = 0, lam = 0
  V2 interaction: iota != 0
  V3 reasoning channel: kappa != 0; splice with R stripped vs R carried
  V4 hidden state: lam != 0 and phi != 0 (U drives both path choice and how the report uses the path)
Diagnostic: self-splice placebo, natural mu(a, a) vs spliced (a -> a).

Run: uv run --no-project --with scipy==1.13.1 --with numpy==1.26.4 python b2_path_splicing.py
"""
import json
import numpy as np
from scipy.special import expit, logit

N_V, RUNS = 400, 200
P_A, P_B = 0.7, 0.3
DELTA, GAMMA = -0.6, -0.3


def simulate(rng, iota=0.0, kappa=0.0, lam=0.0, phi=0.0, carry_R=False):
    theta = rng.standard_normal(N_V)
    eta = 0.3 * rng.standard_normal((N_V, 2))
    beta = {"a": logit(P_A), "b": logit(P_B)}

    def path_phase(f, n):
        U = rng.standard_normal((N_V, n))
        P = (rng.random((N_V, n)) < expit(beta[f] + phi * U)).astype(int)
        return P, U

    def report(f_rep, P, R_is_a, U_rep):
        O = theta[:, None] + DELTA * P + np.take_along_axis(eta, P, axis=1)
        fa = 1.0 if f_rep == "a" else 0.0
        return (O + GAMMA * fa + iota * P * fa + kappa * R_is_a + lam * P * U_rep
                + 0.2 * rng.standard_normal(P.shape))

    out = {}
    # natural runs: reasoning in context repeats the framing; same hidden state in both phases
    for f in "ab":
        P, U = path_phase(f, RUNS)
        out[f"nat_{f}"] = report(f, P, 1.0 * (f == "a"), U).mean()
    # spliced runs
    for fp in "ab":
        for fr in "ab":
            P, U = path_phase(fp, RUNS)
            R_is_a = (1.0 * (fp == "a")) if carry_R else 0.0
            U_rep = rng.standard_normal(P.shape)
            out[f"spl_{fp}{fr}"] = report(fr, P, R_is_a, U_rep).mean()
    # ground truth for the tool-path decomposition (report sees framing f_rep and path only; no R)
    def mu_true(fp, fr):
        if phi == 0:
            pP = P_A if fp == "a" else P_B
            Ebar = theta.mean() + pP * (DELTA + eta[:, 1].mean()) + (1 - pP) * eta[:, 0].mean()
            fa = 1.0 if fr == "a" else 0.0
            return Ebar + GAMMA * fa + iota * pP * fa
        # with phi != 0 the marginal P(P = 1) is E_U expit(beta + phi U); compute by quadrature
        z = np.linspace(-8, 8, 4001)
        w = np.exp(-z ** 2 / 2)
        w /= w.sum()
        pP = float((expit(beta[fp] + phi * z) * w).sum())
        Ebar = theta.mean() + pP * (DELTA + eta[:, 1].mean()) + (1 - pP) * eta[:, 0].mean()
        fa = 1.0 if fr == "a" else 0.0
        return Ebar + GAMMA * fa + iota * pP * fa
    truth = {f"{fp}{fr}": mu_true(fp, fr) for fp in "ab" for fr in "ab"}
    est = {k[4:]: v for k, v in out.items() if k.startswith("spl_")}

    def decomp(c):
        return dict(TE=c["bb"] - c["aa"], IDE_a=c["ab"] - c["aa"], IIE_b=c["bb"] - c["ab"],
                    IIE_a=c["ba"] - c["aa"], IDE_b=c["bb"] - c["ba"],
                    interaction=c["bb"] - c["ba"] - c["ab"] + c["aa"])
    res = dict(truth=decomp(truth), spliced=decomp(est),
               natural_TE=out["nat_b"] - out["nat_a"],
               placebo_aa=out["nat_a"] - est["aa"], placebo_bb=out["nat_b"] - est["bb"])
    return res


def main():
    rng = np.random.default_rng(2026)
    variants = {
        "V1 ideal": dict(),
        "V2 framing x path interaction (iota = -0.4)": dict(iota=-0.4),
        "V3a reasoning channel (kappa = -0.25), R stripped": dict(kappa=-0.25, carry_R=False),
        "V3b reasoning channel (kappa = -0.25), R carried": dict(kappa=-0.25, carry_R=True),
        "V4 hidden state (phi = 1.5, lam = -0.5)": dict(lam=-0.5, phi=1.5),
    }
    allres = {}
    se_cell = None
    for name, kw in variants.items():
        r = simulate(rng, **kw)
        allres[name] = r
        print(f"\n{name}")
        print(f"  natural TE {r['natural_TE']:+.4f} | placebo nat(a,a) - splice(a->a) {r['placebo_aa']:+.4f}, "
              f"nat(b,b) - splice(b->b) {r['placebo_bb']:+.4f}")
        for k in ["TE", "IDE_a", "IIE_b", "IIE_a", "IDE_b", "interaction"]:
            print(f"  {k:12s} truth {r['truth'][k]:+.4f}  spliced {r['spliced'][k]:+.4f}  error {r['spliced'][k] - r['truth'][k]:+.4f}")
    # Monte Carlo standard error of one cell mean: report noise and path randomness over N_V * RUNS runs
    print(f"\nEach cell averages {N_V * RUNS} runs; per-run sd is about 0.4 to 1.1, so a cell's MC SE is about 0.001 to 0.003"
          " (video effects cancel in contrasts because every cell uses the same videos)")
    with open(__file__.replace(".py", "_results.json"), "w") as f:
        json.dump(allres, f, indent=1)


if __name__ == "__main__":
    main()
