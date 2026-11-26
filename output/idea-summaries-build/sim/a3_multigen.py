"""A3 (proposal 06): multi-generation loops in which the edit-effect correlation falls.

Part 1, phenomenological. Each generation proposes one edit with Gaussian (a, b) as in A1, but
rho depends on the cumulative true majority gain G_t: rho(G) = rho_inf + (rho_0 - rho_inf) exp(-G / G0).
Shared improvements are used up as G grows. The mean rule accepts if w a_hat + (1 - w) b_hat > 0.
We compare the Monte Carlo mean tail trajectory with a mean-field recursion built from the A1
formulas, and record whether an inverted U appears and where it peaks.

Part 2, mechanistic (Fisher geometric model). Harness state x in R^d; group losses
L_A = |x - x_A|^2, L_B = |x - x_B|^2; an edit adds delta ~ N(0, tau^2 I). Loss reductions
a = L_A(x) - L_A(x + delta), b likewise, are seen with Gaussian estimation noise. Here rho falls on
its own as the loop approaches the mean optimum x_w = w x_A + (1 - w) x_B. In the small-edit limit
Cov(b, S) is proportional to grad L_B . grad L_w = 4 (x - x_B) . (x - x_w), which is negative exactly
inside the ball whose diameter joins x_B and x_w. We test whether the local-moment drift formula
predicts the realized tail trajectory, and show the three regimes (monotone gain, inverted U,
immediate decline) by start position. We also show attenuation of a naive panel estimate of rho.

Run: uv run --no-project --with scipy==1.13.1 --with numpy==1.26.4 python a3_multigen.py
"""
import json
import numpy as np
from scipy.stats import norm
from scipy.optimize import brentq


def lam(z):
    return np.exp(norm.logpdf(z) - norm.logcdf(z))


def drift_terms(mu_a, mu_b, sa, sb, rho, ea, eb, w):
    """Expected (a 1{S>0}, b 1{S>0}) per proposed edit, Gaussian model (A1)."""
    cov_aS = w * sa ** 2 + (1 - w) * rho * sa * sb
    cov_bS = w * rho * sa * sb + (1 - w) * sb ** 2
    mu_S = w * mu_a + (1 - w) * mu_b
    var_S = w ** 2 * (sa ** 2 + ea ** 2) + (1 - w) ** 2 * (sb ** 2 + eb ** 2) + 2 * w * (1 - w) * rho * sa * sb
    sS = np.sqrt(var_S)
    z = mu_S / sS
    return (mu_a * norm.cdf(z) + cov_aS / sS * norm.pdf(z),
            mu_b * norm.cdf(z) + cov_bS / sS * norm.pdf(z))


def inverted_u(mean_traj, se_traj, k=3.0):
    """Tail performance trajectory (higher is better). Inverted U if an interior peak beats both ends by k SE."""
    t_star = int(np.argmax(mean_traj))
    peak = mean_traj[t_star]
    up = peak - mean_traj[0] > k * max(se_traj[t_star], 1e-12)
    down = peak - mean_traj[-1] > k * np.sqrt(se_traj[t_star] ** 2 + se_traj[-1] ** 2)
    return bool(up and down), t_star


def part1(rng):
    out = []
    sa = sb = 1.0
    mu_a = mu_b = -0.25
    rho0, G0, T, R = 0.8, 20.0, 400, 4000
    v_sd = 1.0
    n_tot = 160
    for w in [0.5, 0.75, 0.875, 0.95]:
        nA, nB = w * n_tot, (1 - w) * n_tot
        ea, eb = v_sd * np.sqrt(1 / nA) * np.sqrt(n_tot / 20), v_sd * np.sqrt(1 / nB) * np.sqrt(n_tot / 20)
        # rho_crit: zero of the tail drift per proposed edit
        f = lambda r: drift_terms(mu_a, mu_b, sa, sb, r, ea, eb, w)[1]
        rho_crit = brentq(f, -0.999, 0.999) if f(-0.999) < 0 < f(0.999) else (np.nan if f(-0.999) > 0 else 1.0)
        for rho_inf in [0.4, 0.0, -0.2, -0.4, -0.8]:
            rhof = lambda G: rho_inf + (rho0 - rho_inf) * np.exp(-np.maximum(G, 0) / G0)
            # mean-field prediction
            G, Tb, pred = 0.0, 0.0, [0.0]
            for t in range(T):
                da, db = drift_terms(mu_a, mu_b, sa, sb, rhof(G), ea, eb, w)
                G += da
                Tb += db
                pred.append(Tb)
            pred = np.array(pred)
            # Monte Carlo
            G = np.zeros(R)
            Tb = np.zeros(R)
            traj = np.zeros((T + 1, R))
            for t in range(T):
                r = rhof(G)
                z1 = rng.standard_normal(R)
                z2 = rng.standard_normal(R)
                a = mu_a + sa * z1
                b = mu_b + sb * (r * z1 + np.sqrt(1 - r ** 2) * z2)
                S = w * (a + ea * rng.standard_normal(R)) + (1 - w) * (b + eb * rng.standard_normal(R))
                acc = S > 0
                G += a * acc
                Tb += b * acc
                traj[t + 1] = Tb
            m = traj.mean(1)
            se = traj.std(1, ddof=1) / np.sqrt(R)
            iu, t_star = inverted_u(m, se)
            iu_pred, t_pred = inverted_u(pred, np.full_like(pred, 1e-3))
            out.append(dict(w=w, rho_inf=rho_inf, rho_crit=float(rho_crit) if np.isfinite(rho_crit) else None,
                            inverted_u_mc=iu, peak_gen_mc=t_star, inverted_u_pred=iu_pred, peak_gen_pred=t_pred,
                            tail_end_mc=float(m[-1]), tail_end_pred=float(pred[-1]),
                            tail_peak_mc=float(m[t_star]), max_abs_traj_err=float(np.abs(m - pred).max()),
                            final_sd_across_runs=float(traj[-1].std())))
    print("Part 1 (phenomenological), rho_0 = 0.8, G0 = 20, mu_a = mu_b = -0.25, sigma_a = sigma_b = 1, T = 400, R = 4000")
    print(" w     rho_inf rho_crit | invU MC (peak) | invU pred (peak) | tail end MC / pred | max|MC-pred| traj")
    for o in out:
        rc = "  n/a " if o["rho_crit"] is None else f"{o['rho_crit']:+.3f}"
        print(f" {o['w']:.3f} {o['rho_inf']:+.1f}    {rc}  | {str(o['inverted_u_mc']):5s} ({o['peak_gen_mc']:3d}) | "
              f"{str(o['inverted_u_pred']):5s} ({o['peak_gen_pred']:3d})   | {o['tail_end_mc']:+8.2f} / {o['tail_end_pred']:+8.2f} | {o['max_abs_traj_err']:.2f}")
    agree = np.mean([o["inverted_u_mc"] == o["inverted_u_pred"] for o in out])
    print(f"agreement of inverted-U call, MC vs mean-field: {agree:.2f}")
    return out


def fgm_moments(x, xA, xB, tau2, d):
    gA = x - xA
    gB = x - xB
    mu = -d * tau2
    vA = 4 * tau2 * (gA * gA).sum(-1) + 2 * d * tau2 ** 2
    vB = 4 * tau2 * (gB * gB).sum(-1) + 2 * d * tau2 ** 2
    cAB = 4 * tau2 * (gA * gB).sum(-1) + 2 * d * tau2 ** 2
    return mu, np.sqrt(vA), np.sqrt(vB), cAB / np.sqrt(vA * vB)


def part2(rng):
    d, Delta, D = 10, 1.0, 3.0
    w = 0.875
    tau = 0.1 / np.sqrt(d)
    tau2 = tau ** 2
    xA = np.zeros(d)
    xB = np.zeros(d)
    xB[0] = Delta
    xw = w * xA + (1 - w) * xB
    u = (xA - xB) / Delta          # points from the tail optimum toward the majority optimum
    vdir = np.zeros(d)
    vdir[1] = 1.0
    T, R = 1500, 400
    results = []
    starts = {
        "majority side (theta = 0)": xw + D * u,
        "perpendicular (theta = 90)": xw + D * vdir,
        "tail side, outside ball (theta = 150)": xw + D * (np.cos(np.deg2rad(150)) * u + np.sin(np.deg2rad(150)) * vdir),
        "tail side, on the axis (theta = 180)": xw - D * u,
        "inside the ball (between x_B and x_w)": xw + 0.5 * (xB - xw) + 0.05 * vdir,
    }
    for noise_sd in [0.0, 0.05]:
        ea = noise_sd * np.sqrt(160 / 140)
        eb = noise_sd * np.sqrt(160 / 20)
        for name, x0 in starts.items():
            x = np.tile(x0, (R, 1))
            LB = np.zeros((T + 1, R))
            LA = np.zeros((T + 1, R))
            pred_db = np.zeros(T)
            rho_t = np.zeros(T)
            rstar_t = np.zeros(T)
            LB[0] = ((x - xB) ** 2).sum(1)
            LA[0] = ((x - xA) ** 2).sum(1)
            for t in range(T):
                mu, sA, sB, r = fgm_moments(x, xA, xB, tau2, d)
                _, db = drift_terms(mu, mu, sA, sB, r, ea, eb, w)
                pred_db[t] = db.mean()             # predicted E[b 1{S>0}] from local Gaussian moments
                rho_t[t] = r.mean()
                rstar_t[t] = np.mean(-(1 - w) * sB / (w * sA))
                delta = tau * rng.standard_normal((R, d))
                xn = x + delta
                a = LA[t] - ((xn - xA) ** 2).sum(1)
                b = LB[t] - ((xn - xB) ** 2).sum(1)
                S = w * (a + ea * rng.standard_normal(R)) + (1 - w) * (b + eb * rng.standard_normal(R))
                acc = (S > 0)[:, None]
                x = np.where(acc, xn, x)
                LB[t + 1] = ((x - xB) ** 2).sum(1)
                LA[t + 1] = ((x - xA) ** 2).sum(1)
            tail_perf = -LB                      # higher is better
            m = tail_perf.mean(1)
            se = tail_perf.std(1, ddof=1) / np.sqrt(R)
            iu, t_star = inverted_u(m, se)
            realized_db = np.diff(tail_perf.mean(1))   # realized mean tail gain per generation (= -Delta L_B)
            pred_cum = np.concatenate([[0], np.cumsum(pred_db)])
            real_cum = m - m[0]
            # first generation at which predicted per-generation tail drift turns negative (after being positive)
            neg = np.where(pred_db < 0)[0]
            t_cross = int(neg[0]) if len(neg) else None
            mean_obj = (w * LA + (1 - w) * LB).mean(1)
            results.append(dict(noise_sd=noise_sd, start=name, inverted_u=iu, peak_gen=t_star,
                                pred_first_negative_gen=t_cross,
                                tail_loss_start=float(LB[0].mean()), tail_loss_min=float(LB.mean(1).min()),
                                tail_loss_end=float(LB[-1].mean()),
                                mean_loss_start=float(mean_obj[0]), mean_loss_end=float(mean_obj[-1]),
                                rho_start=float(rho_t[0]), rho_end=float(rho_t[-1]),
                                rhostar_start=float(rstar_t[0]), rhostar_end=float(rstar_t[-1]),
                                rho_at_peak=float(rho_t[min(t_star, T - 1)]), rhostar_at_peak=float(rstar_t[min(t_star, T - 1)]),
                                rho_at_start_minus_rhostar=float(rho_t[0] - rstar_t[0]),
                                cum_pred_end=float(pred_cum[-1]), cum_real_end=float(real_cum[-1]),
                                max_abs_cum_err=float(np.abs(pred_cum - real_cum).max()),
                                cum_range=float(np.abs(real_cum).max()),
                                corr_per_gen=float(np.corrcoef(pred_db, realized_db)[0, 1])))
    print("\nPart 2 (Fisher geometric model), d = 10, |x_A - x_B| = 1, start distance 3 from x_w, w = 0.875, T = 1500, R = 400")
    for r in results:
        print(f" noise {r['noise_sd']:.2f} | {r['start']:40s} | invU {str(r['inverted_u']):5s} peak {r['peak_gen']:4d} "
              f"pred first harm gen {str(r['pred_first_negative_gen']):>5s} | L_B start/min/end "
              f"{r['tail_loss_start']:.3f}/{r['tail_loss_min']:.3f}/{r['tail_loss_end']:.3f} | mean loss "
              f"{r['mean_loss_start']:.3f}->{r['mean_loss_end']:.3f} | rho {r['rho_start']:+.2f}->{r['rho_end']:+.2f} "
              f"rho* {r['rhostar_start']:+.2f}->{r['rhostar_end']:+.2f} | cum tail pred/real {r['cum_pred_end']:+.3f}/"
              f"{r['cum_real_end']:+.3f} max err {r['max_abs_cum_err']:.3f} of range {r['cum_range']:.3f} | at peak rho {r['rho_at_peak']:+.2f} rho* {r['rhostar_at_peak']:+.2f} | corr(pred, real per gen) {r['corr_per_gen']:.2f}")
    return results


def part3_direct(rng):
    """Estimating the per-edit tail drift E[b 1{S > 0}] from a panel of 200 edits.
    Plug-in: Gaussian formula with noise-corrected moments. Direct: mean of (panel-pool tail gain) x
    (dev-set acceptance indicator); unbiased without any Gaussian assumption because panel noise is
    independent of dev-set noise."""
    out = []
    sa = sb = 1.0
    mu = -0.25
    w = 0.875
    n_edits, reps = 200, 2000
    for rho in [0.6, 0.0, -0.4]:
        for eb in [0.5, 1.0, 2.0]:
            ea = eb * np.sqrt(20 / 140)
            truth = drift_terms(mu, mu, sa, sb, rho, ea, eb, w)[1]
            plug, direct = [], []
            for _ in range(reps):
                z1 = rng.standard_normal(n_edits)
                z2 = rng.standard_normal(n_edits)
                a = mu + sa * z1
                b = mu + sb * (rho * z1 + np.sqrt(1 - rho ** 2) * z2)
                # dev-set estimates (what the loop would see)
                S_dev = w * (a + ea * rng.standard_normal(n_edits)) + (1 - w) * (b + eb * rng.standard_normal(n_edits))
                # panel-pool estimates (disjoint people, same noise level)
                ap = a + ea * rng.standard_normal(n_edits)
                bp = b + eb * rng.standard_normal(n_edits)
                direct.append(np.mean(bp * (S_dev > 0)))
                c = np.cov(ap, bp)
                va, vb = max(c[0, 0] - ea ** 2, 1e-4), max(c[1, 1] - eb ** 2, 1e-4)
                r_hat = np.clip(c[0, 1] / np.sqrt(va * vb), -0.999, 0.999)
                plug.append(drift_terms(ap.mean(), bp.mean(), np.sqrt(va), np.sqrt(vb), r_hat, ea, eb, w)[1])
            out.append(dict(rho=rho, s_b=eb, truth=float(truth), plug_mean=float(np.mean(plug)), plug_sd=float(np.std(plug)),
                            direct_mean=float(np.mean(direct)), direct_sd=float(np.std(direct))))
    print("\nPart 4: estimating per-edit tail drift E[b 1{S>0}] from 200 panel edits (mu = -0.25, w = 0.875)")
    for o in out:
        print(f" rho {o['rho']:+.1f} s_b {o['s_b']:.1f}: truth {o['truth']:+.4f} | plug-in {o['plug_mean']:+.4f} (sd {o['plug_sd']:.4f}) "
              f"| direct {o['direct_mean']:+.4f} (sd {o['direct_sd']:.4f})")
    return out


def part3_panel(rng):
    """Naive vs noise-corrected panel estimates of rho from 200 single edits."""
    out = []
    sa = sb = 1.0
    n_edits = 200
    reps = 2000
    for rho in [0.6, 0.0, -0.4]:
        for eb in [0.5, 1.0, 2.0]:
            ea = eb * np.sqrt(20 / 140)
            naive, corr = [], []
            for _ in range(reps):
                z1 = rng.standard_normal(n_edits)
                z2 = rng.standard_normal(n_edits)
                a = sa * z1
                b = sb * (rho * z1 + np.sqrt(1 - rho ** 2) * z2)
                ah = a + ea * rng.standard_normal(n_edits)
                bh = b + eb * rng.standard_normal(n_edits)
                c = np.cov(ah, bh)
                naive.append(c[0, 1] / np.sqrt(c[0, 0] * c[1, 1]))
                va, vb = max(c[0, 0] - ea ** 2, 1e-6), max(c[1, 1] - eb ** 2, 1e-6)
                corr.append(np.clip(c[0, 1] / np.sqrt(va * vb), -1, 1))
            out.append(dict(rho=rho, noise_b_over_sigma_b=eb, naive_mean=float(np.mean(naive)),
                            corrected_mean=float(np.mean(corr)), corrected_sd=float(np.std(corr)),
                            theory_naive=float(rho * sa * sb / np.sqrt((sa ** 2 + ea ** 2) * (sb ** 2 + eb ** 2)))))
    print("\nPart 3: panel of 200 edits, tail estimation noise s_b in units of sigma_b (s_a = s_b sqrt(20/140))")
    for o in out:
        print(f" rho {o['rho']:+.1f} s_b {o['noise_b_over_sigma_b']:.1f}: naive {o['naive_mean']:+.3f} "
              f"(theory {o['theory_naive']:+.3f}), corrected {o['corrected_mean']:+.3f} (sd {o['corrected_sd']:.3f})")
    return out


def main():
    rng = np.random.default_rng(31)
    p1 = part1(rng)
    p2 = part2(rng)
    p3 = part3_panel(rng)
    p4 = part3_direct(rng)
    with open(__file__.replace(".py", "_results.json"), "w") as f:
        json.dump(dict(part1=p1, part2=p2, part3=p3, part4=p4), f, indent=1)


if __name__ == "__main__":
    main()
