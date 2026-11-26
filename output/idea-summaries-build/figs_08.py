"""Figures for proposal 08 (blind analysis for measurement agents).

Run: python3 -B output/idea-summaries-build/figs_08.py
Writes SVGs to docs/research-plans/images/08/.

Color meaning, fixed across all figures:
  blue   = blind measurement / neutral
  orange = context: the frail referral (framing a), or context in general
  violet = the athlete referral (framing b)
  red    = harm, lost information
Slate and grey are structural ink only.
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import svglib as S  # noqa: E402
from svglib import C, INK, INK2, MUTED, RULE, WHITE  # noqa: E402

ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
OUT = os.path.join(ROOT, 'docs', 'research-plans', 'images', '08')
SIM = os.path.join(HERE, 'sim', 'b1_double_counting_results.json')
os.makedirs(OUT, exist_ok=True)

BLUE, ORANGE, VIOLET, RED, SLATE = C['blue'], C['orange'], C['violet'], C['red'], C['slate']


def box(f, x, y, w, h, role, title=None, lines=(), tsize=15, bsize=14, pad=16, dash=None, tag=None,
        center=False):
    """Card with a bold title and short body lines. Returns bottom y of text."""
    col, bg, dark = C[role]
    f.rect(x, y, w, h, fill=bg, stroke=col, rx=12, sw=1.6, dash=dash)
    yy = y + pad + tsize * S.FS * 0.85
    if tag:
        f.pill(x + pad, y + pad - 4, tag, role, size=12)
        yy += 26
    anchor = 'middle' if center else 'start'
    tx = x + w / 2 if center else x + pad
    if title:
        for ln in S.wrap(title, w - 2 * pad, tsize, 700):
            f.text(tx, yy, ln, tsize, INK, 700, anchor)
            yy += tsize * S.FS * 1.3
    for item in lines:
        for ln in S.wrap(item, w - 2 * pad, bsize):
            f.text(tx, yy + 2, ln, bsize, INK2, 400, anchor)
            yy += bsize * S.FS * 1.38
    return yy


def axes(f, x0, y0, x1, y1, xticks, yticks, xmap, ymap, xlabel, ylabel, fmt_x=str, fmt_y=str):
    """Draw left and bottom axes with ticks. y0 is the top, y1 the bottom (pixel coords)."""
    f.line(x0, y1, x1, y1, INK2, 1.6)
    f.line(x0, y0, x0, y1, INK2, 1.6)
    for t in xticks:
        px = xmap(t)
        f.line(px, y1, px, y1 + 6, INK2, 1.4)
        f.text(px, y1 + 26, fmt_x(t), 13, INK2, 400, 'middle')
    for t in yticks:
        py = ymap(t)
        f.line(x0 - 6, py, x0, py, INK2, 1.4)
        f.line(x0 + 1, py, x1, py, '#eceef1', 1.0)
        f.text(x0 - 12, py + 5, fmt_y(t), 13, INK2, 400, 'end')
    f.text((x0 + x1) / 2, y1 + 58, xlabel, 14, INK, 600, 'middle')
    f.text(x0, y0 - 18, ylabel, 14, INK, 600, 'start')


def polyline(f, pts, color, sw=3, dash=None):
    d = 'M' + ' L'.join(f'{x:.1f},{y:.1f}' for x, y in pts)
    f.path(d, stroke=color, sw=sw, dash=dash)


# ---------------------------------------------------------------------------
# Figure 1: one video, two referrals, two paths, two numbers
# ---------------------------------------------------------------------------
def fig_one_video():
    f = S.Fig(1300, 540, 'One video, two referrals, two measurements',
              'The same single-leg stance video is analyzed under two referrals. Each referral leads the agent '
              'to a different but defensible analysis path and a different hold time. Illustrative.')
    # video card
    vx, vy, vw, vh = 40, 140, 240, 264
    f.rect(vx, vy, vw, vh, fill=C['white'][1], stroke=INK2, rx=12, sw=1.6)
    f.text(vx + vw / 2, vy + 34, 'Same video', 16, INK, 700, 'middle')
    cx, top = vx + vw / 2, vy + 70
    col = INK2
    f.circle(cx, top + 12, 12, fill=WHITE, stroke=col, sw=2.4)
    f.line(cx, top + 25, cx, top + 92, col, 2.6)
    f.line(cx, top + 40, cx - 42, top + 52, col, 2.6)
    f.line(cx, top + 40, cx + 42, top + 52, col, 2.6)
    f.line(cx, top + 92, cx - 4, top + 150, col, 2.6)
    f.line(cx, top + 92, cx + 30, top + 112, col, 2.6)
    f.line(cx + 30, top + 112, cx + 20, top + 136, col, 2.6)
    f.line(vx + 50, top + 152, vx + vw - 50, top + 152, RULE, 2)
    f.text(vx + vw / 2, vy + vh - 18, 'single-leg stance', 14, MUTED, 400, 'middle')

    # run cards
    rx, rw = 350, 530
    rows = [(60, 'orange', 'Referral: suspected Parkinson\'s, recent falls',
             ['Timing: stops at the first large sway', 'Filter: low-pass at 3 Hz'], 'Shorter hold time'),
            (300, 'violet', 'Referral: routine screening, no balance concerns',
             ['Timing: continues after balance recovers', 'Filter: low-pass at 6 Hz'], 'Longer hold time')]
    for ry, role, ref, path, rep in rows:
        col_, bg, dark = C[role]
        f.rect(rx, ry, rw, 180, fill=WHITE, stroke=col_, rx=12, sw=1.8)
        f.rect(rx, ry, rw, 52, fill=bg, stroke=col_, rx=12, sw=1.8)
        f.rect(rx + 1, ry + 30, rw - 2, 22, fill=bg, stroke=bg, rx=0, sw=0)
        f.line(rx, ry + 52, rx + rw, ry + 52, col_, 1.6)
        f.text(rx + 18, ry + 34, ref, 15, dark, 700)
        for i, p in enumerate(path):
            f.circle(rx + 26, ry + 100 + i * 40 - 5, 4, fill=col_, stroke=col_)
            f.text(rx + 42, ry + 100 + i * 40, p, 15, INK2)
        # report card
        px = 960
        f.rect(px, ry + 40, 300, 100, fill=bg, stroke=col_, rx=12, sw=1.8)
        f.text(px + 150, ry + 98, rep, 18, dark, 700, 'middle')
        f.arrow([(rx + rw, ry + 90), (px - 8, ry + 90)], color=col_, sw=2.4)
    f.arrow([(vx + vw, vy + 85), (rx - 8, 150)], color=INK2, sw=2.2)
    f.arrow([(vx + vw, vy + 165), (rx - 8, 390)], color=INK2, sw=2.2)
    f.text(vx + vw / 2, vy - 16, 'illustrative example', 15, MUTED, 600, 'middle', italic=True)
    f.save(os.path.join(OUT, 'one-video-two-referrals.svg'))


# ---------------------------------------------------------------------------
# Figure 2: the referral is counted twice
# ---------------------------------------------------------------------------
def fig_counted_twice():
    f = S.Fig(1300, 470, 'The referral is counted twice',
              'The referral sets the clinician prior and also shapes the agent measurement; the combiner then '
              'treats the measurement as independent evidence.')
    box(f, 40, 85, 250, 90, 'orange', 'Referral H', ['suspected Parkinson\'s'])
    box(f, 40, 315, 250, 90, 'blue', 'Video', ['single-leg stance'])
    box(f, 420, 85, 270, 90, 'orange', 'Prior from referral', ['clinician\'s starting odds'])
    box(f, 420, 295, 270, 130, 'white', 'Measurement agent',
        ['sees video and referral', 'hold time M pulled', 'toward the referral'])
    box(f, 770, 165, 290, 140, 'white', 'Combiner', ['prior odds × likelihood ratio', 'fitted on blind reports'])
    box(f, 1100, 165, 170, 140, 'red', 'Posterior', ['can be overconfident', 'when H is wrong'])
    f.arrow([(290, 130), (418, 130)], color=ORANGE[0], sw=2.6)
    f.text(354, 118, 'count 1', 14, ORANGE[2], 600, 'middle')
    f.arrow([(290, 168), (418, 322)], color=ORANGE[0], sw=2.6)
    f.text(350, 262, 'count 2', 14, ORANGE[2], 600, 'end')
    f.arrow([(290, 360), (418, 360)], color=BLUE[0], sw=2.4)
    f.arrow([(690, 140), (768, 205)], color=INK2, sw=2.2)
    f.arrow([(690, 350), (768, 265)], color=ORANGE[0], sw=2.6)
    f.text(718, 348, 'referral-shaped M', 15, ORANGE[2], 600, 'start')
    f.arrow([(1060, 235), (1098, 235)], color=INK2, sw=2.2)
    f.save(os.path.join(OUT, 'referral-counted-twice.svg'))


# ---------------------------------------------------------------------------
# Figure 3: better measurer, worse decision (computed from sim/b1)
# ---------------------------------------------------------------------------
def fig_better_measurer():
    d = json.load(open(SIM))
    curve = d['curve']
    g = [c['g'] for c in curve]
    pen = [c['penalty'] for c in curve]
    f = S.Fig(1300, 540, 'Better measurer, worse decision',
              'Computed for the worked example: mean squared error of the shrunk measurement falls below the blind '
              'report for small shrinkage while the decision log-loss penalty of a blind-calibrated combiner rises '
              'from zero.')
    L = dict(x0=130, x1=590, y0=110, y1=410)
    R = dict(x0=790, x1=1250, y0=110, y1=410)

    def mk(P, ymax):
        xm = lambda t: P['x0'] + (P['x1'] - P['x0']) * t
        ym = lambda v: P['y1'] - (P['y1'] - P['y0']) * v / ymax
        return xm, ym

    def axes2(P, xm, ym, yt, fmt_y, title, sub):
        f.line(P['x0'], P['y1'], P['x1'], P['y1'], INK2, 1.6)
        f.line(P['x0'], P['y0'], P['x0'], P['y1'], INK2, 1.6)
        for t in [0, 0.25, 0.5, 0.75, 1.0]:
            f.line(xm(t), P['y1'], xm(t), P['y1'] + 6, INK2, 1.4)
            f.text(xm(t), P['y1'] + 26, f'{t:g}', 13, INK2, 400, 'middle')
        for t in yt:
            f.line(P['x0'] - 6, ym(t), P['x0'], ym(t), INK2, 1.4)
            f.text(P['x0'] - 12, ym(t) + 5, fmt_y(t), 13, INK2, 400, 'end')
        f.text((P['x0'] + P['x1']) / 2, P['y1'] + 58, 'shrinkage toward the referral, γ', 14, INK, 600, 'middle')
        f.text(P['x0'], P['y0'] - 44, title, 15, INK, 700, 'start')
        if sub:
            f.text(P['x0'], P['y0'] - 20, sub, 13, INK2, 400, 'start')

    gs = 0.357
    mse = lambda t: (1 - t) ** 2 + 1.8 * t * t
    # left panel: MSE (closed form, blind = 1), points from the simulation
    xm, ym = mk(L, 2.0)
    # shade only where the curve is below the blind baseline (0 < gamma < 2 gamma*)
    pts = [(xm(i / 200 * 2 * gs), ym(mse(i / 200 * 2 * gs))) for i in range(201)]
    dpath = 'M' + ' L'.join(f'{x:.1f},{y:.1f}' for x, y in pts) + ' Z'
    f.path(dpath, stroke='none', sw=0, fill='#eceef1')
    axes2(L, xm, ym, [0, 0.5, 1.0, 1.5, 2.0], lambda t: f'{t:g}', 'Measurement error (MSE)',
          'relative to the blind report')
    f.line(xm(gs), L['y0'] + 30, xm(gs), L['y1'], INK2, 1.4, dash='5 5')
    f.line(L['x0'], ym(1.0), L['x1'], ym(1.0), INK2, 1.6, dash='8 5')
    f.text(L['x0'] + 10, ym(1.0) - 10, 'blind report', 13, INK2, 600, 'start')
    polyline(f, [(xm(i / 100), ym(mse(i / 100))) for i in range(101)], INK2, 3)
    for gi, c in zip(g, curve):
        f.circle(xm(gi), ym(c['mse']), 4.5, fill=INK2, stroke=WHITE, sw=1.2)
    f.text(xm(gs), L['y0'] + 18, 'γ* = 0.357', 13, INK, 600, 'middle')
    f.text(xm(gs) + 14, ym(0.643) + 30, '36% lower MSE at γ*', 13, INK, 600, 'start')
    # the squared-error-optimal (Bayes) report: effective shrinkage gamma_B = 0.214, MSE ratio 0.614
    gb = 0.214
    diamond = lambda cx, cy, r: f.path(f'M{cx},{cy - r} L{cx + r},{cy} L{cx},{cy + r} L{cx - r},{cy} Z',
                                       stroke=INK, sw=2.2, fill=WHITE)
    diamond(xm(gb), ym(0.614), 9)
    f.text(xm(gb) - 4, ym(0.614) + 30, 'Bayes report', 13, INK, 600, 'middle')

    xm2, ym2 = mk(R, 0.22)
    axes2(R, xm2, ym2, [0, 0.05, 0.10, 0.15, 0.20], lambda t: f'{t:.2f}', 'Decision log-loss penalty (nats)',
          'combiner calibrated on blind reports')
    f.line(xm2(gs), R['y0'] + 30, xm2(gs), R['y1'], INK2, 1.4, dash='5 5')
    polyline(f, [(xm2(a), ym2(b)) for a, b in zip(g, pen)], RED[0], 3)
    for a, b in zip(g, pen):
        f.circle(xm2(a), ym2(b), 4.5, fill=RED[0], stroke=WHITE, sw=1.2)
    f.text(xm2(gs), R['y0'] + 18, 'γ*', 13, INK, 600, 'middle')
    f.text(xm2(gs) + 12, ym2(0.0262) + 6, '+0.026 nats at γ*', 13, RED[2], 600, 'start')
    diamond(xm2(gb), ym2(0.019), 9)
    f.text(xm2(gb) - 4, ym2(0.019) - 22, 'Bayes report', 13, INK, 600, 'middle')
    f.text(650, 526, 'computed in simulation, not measured', 13, MUTED, 400, 'middle', italic=True)
    f.save(os.path.join(OUT, 'better-measurer-worse-decision.svg'))


# ---------------------------------------------------------------------------
# Figure 4: calibration bug or information bug (schematic)
# ---------------------------------------------------------------------------
def fig_two_routes():
    f = S.Fig(1300, 530, 'One-to-one or many-to-one',
              'Left: shifting the number toward the referral is one-to-one within each referral. Right: '
              'a cap under the high-risk referral merges many blind values into one reported value. Schematic.')
    L = dict(x0=130, x1=580, y0=130, y1=420)
    R = dict(x0=790, x1=1240, y0=130, y1=420)
    for P, title in [(L, 'One-to-one: a shift that recalibration can undo'),
                     (R, 'Many-to-one: a cap that erases differences')]:
        f.line(P['x0'], P['y1'], P['x1'], P['y1'], INK2, 1.6)
        f.line(P['x0'], P['y0'], P['x0'], P['y1'], INK2, 1.6)
        f.text(P['x0'], 70, title, 17, INK, 700)
        f.text((P['x0'] + P['x1']) / 2, P['y1'] + 34, 'blind measurement M₀', 14, INK, 600, 'middle')
        f.text(P['x0'], P['y0'] - 18, 'reported M', 14, INK, 600)
    f.text(1240, 34, 'schematic', 14, MUTED, 600, 'end', italic=True)
    # left: two parallel lines of slope (1 - gamma); labels sit just beside their own line
    polyline(f, [(L['x0'] + 10, L['y1'] - 40), (L['x1'] - 20, L['y0'] + 70)], ORANGE[0], 3.2)
    polyline(f, [(L['x0'] + 10, L['y1'] - 95), (L['x1'] - 20, L['y0'] + 15)], VIOLET[0], 3.2)
    f.text(420, 194, 'routine referral b', 14, VIOLET[2], 600, 'end')
    f.text(300, 338, 'high-risk referral a', 14, ORANGE[2], 600, 'start')
    f.text((L['x0'] + L['x1']) / 2, L['y1'] + 80, 'undone by recalibrating within each referral', 14, INK, 600, 'middle')
    # right: identity for the routine referral, a cap for the high-risk referral; below the cap the two coincide
    x0, y1 = R['x0'], R['y1']
    w2 = R['x1'] - R['x0']
    pa, pb = (x0 + 10, y1 - 22), (R['x1'] - 20, R['y0'] + 8)
    cxp = x0 + 0.48 * w2
    yc = pa[1] + (cxp - pa[0]) * (pb[1] - pa[1]) / (pb[0] - pa[0])
    polyline(f, [pa, (cxp, yc)], INK2, 3.4, dash=None)
    polyline(f, [(cxp, yc), pb], VIOLET[0], 3.0, dash='10 7')
    # two different blind values that land on the same report
    for gx in (1075, 1215):
        f.line(gx, y1, gx, yc + 6, RED[0], 1.4, dash='4 4')
    polyline(f, [(cxp, yc), (R['x1'] - 20, yc)], ORANGE[0], 4.2)
    f.circle(cxp, yc, 5, fill=ORANGE[0], stroke=WHITE, sw=1.2)
    for gx in (1075, 1215):
        f.circle(gx, yc, 5.5, fill=WHITE, stroke=RED[0], sw=2.2)
    f.text(1145, yc + 44, 'different M₀,', 13, RED[2], 600, 'middle')
    f.text(1145, yc + 66, 'same report', 13, RED[2], 600, 'middle')
    f.text(1150, 170, 'routine referral b', 14, VIOLET[2], 600, 'end')
    f.text(1238, yc - 12, 'high-risk referral a', 13, ORANGE[2], 600, 'end')
    f.text(872, 384, 'both referrals', 14, INK2, 600, 'start')
    f.text(872, 404, 'below the cap', 14, INK2, 600, 'start')
    f.text(R['x0'] + w2 / 2, R['y1'] + 80, 'many-to-one above the cap', 14, RED[2], 600, 'middle')
    f.save(os.path.join(OUT, 'calibration-bug-or-information-bug.svg'))


# ---------------------------------------------------------------------------
# Figure 5: path splicing as a two-by-two factorial
# ---------------------------------------------------------------------------
def rich(f, x, y, parts, size, color, weight=600, anchor='start', ssize=None):
    """One text element; parts are (string, is_subscript). Subscripts drop by dy and shrink."""
    fs = size * S.FS
    ss = (ssize or round(size * 0.82)) * S.FS
    out, low = [], False
    for t, sub in parts:
        if sub and not low:
            out.append(f'<tspan dy="{fs * 0.28:.1f}" font-size="{ss:.1f}">{S.esc(t)}</tspan>')
            low = True
        elif not sub and low:
            out.append(f'<tspan dy="{-fs * 0.28:.1f}">{S.esc(t)}</tspan>')
            low = False
        else:
            out.append(f'<tspan>{S.esc(t)}</tspan>')
    f.add(f'<text x="{x:.1f}" y="{y:.1f}" font-size="{fs:.1f}" font-weight="{weight}" fill="{color}" '
          f'text-anchor="{anchor}">{"".join(out)}</text>')


def fig_splicing():
    f = S.Fig(1300, 490, 'Path splicing as a two-by-two factorial',
              'Cached transcripts recorded under one referral are replayed into a stateless report step under '
              'either referral. Rows fix the referral during the path, columns the referral at the report step; '
              'diagonal self-splices are checked against natural runs.')
    cw, chh = 230, 110
    cols = [300, 650]
    rows = [110, 340]
    f.text(cols[0] + cw / 2, 86, 'Report step told a (high risk)', 15, ORANGE[2], 700, 'middle')
    f.text(cols[1] + cw / 2, 86, 'Report step told b (routine)', 15, VIOLET[2], 700, 'middle')
    for r, (t1, t2, role) in enumerate([('Path run under a', '(high risk)', 'orange'),
                                         ('Path run under b', '(routine)', 'violet')]):
        yy = rows[r] + chh / 2
        f.text(cols[0] - 24, yy - 4, t1, 15, C[role][2], 700, 'end')
        f.text(cols[0] - 24, yy + 20, t2, 14, C[role][2], 400, 'end')
    cells = {(0, 0): ('μ(a, a)', ['self-splice:', 'check vs natural run'], False),
             (0, 1): ('μ(a, b)', ['cross-splice'], True),
             (1, 0): ('μ(b, a)', ['cross-splice'], True),
             (1, 1): ('μ(b, b)', ['self-splice:', 'check vs natural run'], False)}
    for (r, c), (lab, sub, sp) in cells.items():
        x, yy = cols[c], rows[r]
        f.rect(x, yy, cw, chh, fill=SLATE[1] if sp else WHITE, stroke=INK2, rx=10, sw=1.6, dash='6 4')
        f.text(x + cw / 2, yy + 44, lab, 20, INK, 700, 'middle')
        for i, s in enumerate(sub):
            f.text(x + cw / 2, yy + 72 + i * 20, s, 14, INK2, 400, 'middle')
    # rightward = change the report referral (direct); downward = change the path referral (indirect)
    for r, sub in ((0, 'a'), (1, 'b')):
        yy = rows[r] + chh / 2
        f.arrow([(cols[0] + cw, yy), (cols[1] - 8, yy)], color=INK, sw=2.4)
        mx = (cols[0] + cw + cols[1]) / 2
        f.text(mx, yy - 14, 'direct', 15, INK, 700, 'middle')
        rich(f, mx, yy + 30, [('DE', 0), (sub, 1)], 17, INK2, 600, 'middle', ssize=15)
    yv0, yv1 = rows[0] + chh, rows[1] - 8
    for c, sub, side in ((0, 'a', -1), (1, 'b', 1)):
        cx = cols[c] + cw / 2
        f.arrow([(cx, yv0), (cx, yv1)], color=INK, sw=2.4)
        anc = 'end' if side < 0 else 'start'
        f.text(cx + side * 14, (yv0 + yv1) / 2 - 4, 'indirect', 15, INK, 700, anc)
        rich(f, cx + side * 14, (yv0 + yv1) / 2 + 22, [('IE', 0), (sub, 1)], 17, INK2, 600, anc, ssize=15)

    # right: what one cross-splice is, beside its cell; the interaction beside the bottom row
    ex, ew = 940, 330
    box(f, ex, rows[0], ew, chh, 'white', 'Cells: μ(path, report)',
        ['→ direct: report referral changes', '↓ indirect: path referral changes'], tsize=15, bsize=14)
    f.rect(ex, rows[1], ew, chh, fill=WHITE, stroke=RULE, rx=12, sw=1.6)
    f.text(ex + 16, rows[1] + 36, 'Interaction', 15, INK, 700)
    rich(f, ex + 16, rows[1] + 76, [('DE', 0), ('b', 1), (' − DE', 0), ('a', 1), (' = IE', 0), ('b', 1),
                                    (' − IE', 0), ('a', 1)], 16, INK2, 600, ssize=14)
    f.save(os.path.join(OUT, 'path-splicing-factorial.svg'))


# ---------------------------------------------------------------------------
# Figure 6: the blind-analysis harness
# ---------------------------------------------------------------------------
def fig_harness():
    f = S.Fig(1300, 360, 'Blind measurement, then interpretation',
              'The measurement stage sees no referral and an appearance-masked input; its path and number are '
              'committed before the referral is revealed to the interpretation stage.')
    y, h = 190, 140
    xs = [(40, 230), (300, 230), (560, 190), (780, 260), (1070, 190)]
    box(f, 40, y, 230, h, 'blue', 'Masked input', ['skeleton render', 'no face, no cane'])
    box(f, 300, y, 230, h, 'blue', 'Blind measurement', ['agent and tools', 'no referral in context'])
    box(f, 560, y, 190, h, 'white', 'Commit', ['path and number', 'hashed and frozen'])
    f.lock(712, y + 14, 1.2, color=INK2)
    box(f, 780, y, 260, h, 'orange', 'Interpretation',
        ['sees the referral', 'pre-declared menu only', 'commit is never edited'])
    box(f, 1070, y, 190, h, 'orange', 'Decision', ['evidence: commit', 'prior: referral,', 'used once'])
    box(f, 780, 40, 260, 90, 'orange', 'Referral', ['unlocked after commit'])
    for (x, w), (x2, _) in zip(xs, xs[1:]):
        f.arrow([(x + w, y + h / 2), (x2 - 2, y + h / 2)], color=INK2, sw=2.4)
    f.arrow([(910, 130), (910, y - 2)], color=ORANGE[0], sw=2.6)
    f.save(os.path.join(OUT, 'blind-analysis-harness.svg'))


# ---------------------------------------------------------------------------
# Figure 7: self-improvement experiment design
# ---------------------------------------------------------------------------
def fig_design():
    f = S.Fig(1300, 604, 'Self-improvement under three rewards',
              'Three optimizers run under three rewards on development people only, with most seeds in the main '
              'arm; six checkpoints of each of the 45 runs are audited on sealed test people.')
    # split bar
    f.rect(40, 50, 900, 80, fill=WHITE, stroke=SLATE[0], rx=12, sw=1.6)
    f.text(64, 86, 'Development people', 16, INK, 700)
    f.text(64, 112, 'optimizers run, select and train here', 14, INK2)
    f.rect(960, 50, 300, 80, fill=SLATE[1], stroke=SLATE[0], rx=12, sw=1.6)
    f.lock(980, 70, 1.3, color=INK2)
    f.text(1010, 86, 'Sealed test people', 16, INK, 700)
    f.text(1010, 112, 'audits only', 14, INK2)

    # design line, then reward headers with each arm's role inside its card
    gx, gw, gap = 200, 236, 14
    f.text(gx, 176, '3 optimizers × 15 seeds = 45 runs', 16, INK, 700)
    heads = [('orange', '(a) Accuracy', ['informative referral', 'main arm', '8 seeds']),
             ('slate', '(b) Approval judge', ['sees the referral', 'positive control', '3 seeds']),
             ('white', '(c) Accuracy', ['randomized referral', 'control', '4 seeds'])]
    for i, (role, t1, ls) in enumerate(heads):
        x = gx + i * (gw + gap)
        box(f, x, 196, gw, 124, role, t1, ls, tsize=15, bsize=14, pad=14)
    rlabels = [('GEPA', 'prompt evolution'), ('ACE', 'playbook'), ('GRPO', 'weights')]
    r0, rh = 340, 78
    for r, (n1, n2) in enumerate(rlabels):
        yy = r0 + r * rh
        f.text(40, yy + 32, n1, 16, INK, 700)
        f.text(40, yy + 56, n2, 13, INK2)
        for i in range(3):
            x = gx + i * (gw + gap)
            f.rect(x, yy, gw, 64, fill=WHITE, stroke=RULE, rx=10, sw=1.4)
            nk = (8, 3, 4)[i]
            for k in range(nk):
                f.circle(x + gw / 2 + (k - (nk - 1) / 2) * 24, yy + 32, 7, fill=INK2, stroke=INK2, sw=1)
    # bracket enclosing all nine cells, feeding the audit card
    bx, by0, by1 = gx + 3 * gw + 2 * gap + 22, r0, r0 + 2 * rh + 64
    f.path(f'M{bx - 8},{by0} L{bx},{by0} L{bx},{by1} L{bx - 8},{by1}', stroke=INK2, sw=2)
    mid = (by0 + by1) / 2
    ax, aw, ah = 1000, 260, 130
    ay = mid - ah / 2
    f.rect(ax, ay, aw, ah, fill=WHITE, stroke=RULE, rx=12, sw=1.6)
    f.text(ax + 16, ay + 40, 'Audit 6 checkpoints', 16, INK, 700)
    f.text(ax + 16, ay + 66, 'per run', 16, INK, 700)
    f.text(ax + 16, ay + 100, 'on sealed test people', 14, INK2)
    f.arrow([(bx, mid), (ax - 2, mid)], color=INK2, sw=2.2)
    f.arrow([(1130, 130), (1130, ay - 2)], color=INK2, sw=2.2)
    f.save(os.path.join(OUT, 'self-improvement-design.svg'))


# ---------------------------------------------------------------------------
# Figure 8: predicted routes by optimizer (hypothetical)
# ---------------------------------------------------------------------------
def fig_predicted():
    f = S.Fig(1300, 500, 'Where each optimizer puts the context',
              'Hypothetical pre-registered predictions at the final checkpoint: under accuracy reward both '
              'optimizer types reach the predicted shrinkage band, but only prompt and playbook evolution put '
              'most of the framing effect through the analysis path.')
    f.text(40, 40, 'Hypothetical, pre-registered predictions at the final checkpoint', 15, MUTED, 700, italic=True)
    f.text(40, 70, 'Under reward (a) both optimizer types reach the band; only GEPA and ACE put most of it '
           'through the path', 15, INK, 700)
    x0, x1, lo, hi = 330, 1110, -0.05, 0.35
    xm = lambda v: x0 + (x1 - x0) * (v - lo) / (hi - lo)
    top, axy = 150, 420
    gB = 0.214
    # H4 band and gamma_B reference, behind the bars
    f.rect(xm(gB - 0.1), top, xm(gB + 0.1) - xm(gB - 0.1), axy - top, fill='#eceef1', stroke='#eceef1', rx=0, sw=0)
    f.line(xm(gB), top, xm(gB), axy, MUTED, 1.4)
    rich(f, xm(gB), top - 12, [('H4 band: γ', 0), ('B', 1), (' ± 0.1', 0)], 14, INK2, 600, 'middle', ssize=12)
    # legend
    f.rect(40, 100, 26, 16, fill=ORANGE[0], stroke=ORANGE[0], rx=3, sw=1.2)
    f.text(74, 114, 'through the path (indirect)', 14, INK2, 600)
    f.rect(330, 100, 26, 16, fill=ORANGE[1], stroke=ORANGE[0], rx=3, sw=1.2)
    f.text(364, 114, 'direct', 14, INK2, 600)
    rows = [('GEPA, ACE', 'reward (a)', 0.24, 0.185, 'mostly through the path'),
            ('GRPO', 'reward (a)', 0.205, 0.025, 'mostly direct'),
            ('All optimizers', 'reward (c)', 0.0, 0.0, 'no framing effect')]
    bh = 40
    f.line(xm(0), top, xm(0), axy, INK2, 1.4, dash='3 4')
    for i, (n1, n2, tot, ind, lab) in enumerate(rows):
        yc = 200 + i * 85
        f.text(300, yc - 2, n1, 16, INK, 700, 'end')
        f.text(300, yc + 20, n2, 13, INK2, 400, 'end')
        if tot > 0:
            f.rect(xm(0), yc - bh / 2, xm(tot) - xm(0), bh, fill=ORANGE[1], stroke=ORANGE[0], rx=4, sw=1.6)
            f.rect(xm(0), yc - bh / 2, xm(ind) - xm(0), bh, fill=ORANGE[0], stroke=ORANGE[0], rx=4, sw=1.6)
            f.text(xm(gB + 0.1) + 14, yc + 5, lab, 14, ORANGE[2], 700)
        else:
            f.circle(xm(0), yc, 7, fill=WHITE, stroke=INK2, sw=2.4)
            f.text(xm(0) + 18, yc + 5, lab, 14, INK2, 700)
    # axis
    f.line(x0, axy, x1, axy, INK2, 1.6)
    for t in (0, 0.1, 0.2, 0.3):
        f.line(xm(t), axy, xm(t), axy + 6, INK2, 1.4)
        f.text(xm(t), axy + 26, f'{t:g}', 13, INK2, 400, 'middle')
    f.text((x0 + x1) / 2, axy + 58, 'framing effect ÷ gap between the referral classes’ means', 14, INK, 600, 'middle')
    f.save(os.path.join(OUT, 'predicted-routes-by-optimizer.svg'))


if __name__ == '__main__':
    fig_one_video()
    fig_counted_twice()
    fig_better_measurer()
    fig_two_routes()
    fig_splicing()
    fig_harness()
    fig_design()
    fig_predicted()
    print('wrote', sorted(os.listdir(OUT)))
