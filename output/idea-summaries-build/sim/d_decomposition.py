"""D (proposal 07): information term and perceptual term of an encoding's error.

Target y = sway amplitude A ~ U(1, 5) (cm). Squared loss. The tool output o reveals A exactly, so R(o) = 0.
Encodings (what the reader sees):
  e_pos(H): position on a common scale, a plot H pixels tall with an autoscaled axis: the drawn bar height is
            round(A c / step) pixels, step = 5 / H, axis scale c ~ U(0.5, 2) shown by tick labels.
  e_area(H): same quantization but the value is drawn as a disc area.
Bayes risk R(e) = E Var(A | rendered pixels): computed exactly by enumerating the posterior over A on a fine grid.
Readers:
  pos reader : y_hat = x_read with Weber-like noise, x_read = value * exp(0.03 xi)
  area reader: Stevens compression, perceived = value^0.7 * exp(0.10 xi), reported on the value scale with a fixed
               linear map fitted to small values (a systematic misreading)
Oracle decoder: k-nearest-neighbour regression on (bar pixels, axis scale) trained on n_train renders, as a
stand-in for a CNN trained on renders. Measured perceptual gap P_hat = R_reader - R_oracle(n_train).
Calibration split: P = [R_reader - R_recalibrated reader] + [R_recalibrated reader - R(e)], recalibration = quadratic polynomial fitted on a separate calibration sample.

Run: uv run --no-project --with scipy==1.13.1 --with numpy==1.26.4 python d_decomposition.py
"""
import json
import numpy as np


def render(A, c, H):
    step = 5.0 / H
    return np.round(A * c / step)          # integer pixel height (or pixel area index)


def bayes_risk(H, n=200_000, rng=None):
    """E Var(A | pixels, c) with A ~ U(1,5): given (k, c) the posterior is uniform on the cell
    {A : round(A c / step) = k} intersected with [1, 5], so Var = width^2 / 12."""
    A = rng.uniform(1, 5, n)
    c = rng.uniform(0.5, 2, n)
    step = 5.0 / H
    k = render(A, c, H)
    lo = np.maximum((k - 0.5) * step / c, 1.0)
    hi = np.minimum((k + 0.5) * step / c, 5.0)
    return float((((hi - lo) ** 2) / 12).mean())


def knn_oracle(train_x, train_y, test_x, k=10):
    preds = np.empty(len(test_x))
    for i0 in range(0, len(test_x), 500):
        d = ((test_x[i0:i0 + 500, None, :] - train_x[None, :, :]) ** 2).sum(-1)
        idx = np.argpartition(d, k, axis=1)[:, :k]
        preds[i0:i0 + 500] = train_y[idx].mean(1)
    return preds


def main():
    rng = np.random.default_rng(707)
    out = []
    n_test = 4000
    for H in [20, 100]:
        RB = bayes_risk(H, rng=rng)
        A = rng.uniform(1, 5, n_test)
        c = rng.uniform(0.5, 2, n_test)
        k = render(A, c, H)
        step = 5.0 / H
        value = k * step / c                      # the value a perfect reader would read off the axis
        # readers
        pos = value * np.exp(0.03 * rng.standard_normal(n_test))
        perceived = value ** 0.7 * np.exp(0.10 * rng.standard_normal(n_test))
        area = 1.0 + (perceived - 1.0) / 0.7      # linearization of v^0.7 at v = 1: a systematic misreading
        res = dict(H=H, bayes_risk=RB)
        for name, yhat in [("position", pos), ("area", area)]:
            R = float(((yhat - A) ** 2).mean())
            # quadratic recalibration fitted on a separate calibration sample
            Ac = rng.uniform(1, 5, n_test)
            cc = rng.uniform(0.5, 2, n_test)
            vc = render(Ac, cc, H) * step / cc
            if name == "position":
                yc = vc * np.exp(0.03 * rng.standard_normal(n_test))
            else:
                yc = 1.0 + (vc ** 0.7 * np.exp(0.10 * rng.standard_normal(n_test)) - 1.0) / 0.7
            X = np.vstack([np.ones(n_test), yc, yc ** 2]).T
            beta = np.linalg.lstsq(X, Ac, rcond=None)[0]
            R_recal = float(((np.vstack([np.ones(n_test), yhat, yhat ** 2]).T @ beta - A) ** 2).mean())
            res[name] = dict(R_reader=R, P_true=R - RB, P_calibration=R - R_recal, P_resolution=R_recal - RB)
        # oracle learning curve
        test_x = np.vstack([k / H, c]).T
        curve = []
        for n_train in [200, 1000, 5000, 20000]:
            At = rng.uniform(1, 5, n_train)
            ct = rng.uniform(0.5, 2, n_train)
            kt = render(At, ct, H)
            tx = np.vstack([kt / H, ct]).T
            pred = knn_oracle(tx, At, test_x)
            R_or = float(((pred - A) ** 2).mean())
            curve.append(dict(n_train=n_train, R_oracle=R_or,
                              P_hat_position=res["position"]["R_reader"] - R_or,
                              P_hat_area=res["area"]["R_reader"] - R_or))
        res["oracle_curve"] = curve
        out.append(res)
        print(f"\nH = {H} pixels: Bayes risk of the encoding R(e) = {RB:.5f} cm^2 (tool floor R(o) = 0)")
        for name in ["position", "area"]:
            r = res[name]
            print(f"  {name:8s} reader: R = {r['R_reader']:.4f} = I {RB:.4f} + P {r['P_true']:.4f}; "
                  f"P = calibration {r['P_calibration']:.4f} + resolution {r['P_resolution']:.4f}")
        for cpt in curve:
            print(f"  oracle n_train = {cpt['n_train']:5d}: R_oracle = {cpt['R_oracle']:.5f} "
                  f"(excess over Bayes {cpt['R_oracle'] - RB:+.5f}); measured P position {cpt['P_hat_position']:.4f}, area {cpt['P_hat_area']:.4f}")
    with open(__file__.replace(".py", "_results.json"), "w") as f:
        json.dump(out, f, indent=1)


if __name__ == "__main__":
    main()
