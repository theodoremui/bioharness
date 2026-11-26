"""Figures for proposal 06, 'Who does self-improvement leave behind?'.

Colour roles, used the same way in every figure:
  blue   = majority people, the mean objective, the loop itself
  orange = the tail (the minority) and harm to it
  aqua   = sealed test data and valid rules
  slate  = neutral structure (axes, arrows, rejected candidates, the guard set)
"""
import math
import os
import random
import sys

sys.path.insert(0, os.path.dirname(__file__))
from svglib import Fig, C, INK, INK2, MUTED, RULE, WHITE, FS, esc, tw  # noqa: E402

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
OUT = os.path.join(ROOT, 'docs', 'idea-summaries', 'images', '06')
os.makedirs(OUT, exist_ok=True)

BLUE, ORANGE, AQUA, SLATE = C['blue'], C['orange'], C['aqua'], C['slate']


def mtext(f, x, y, parts, size=14, fill=INK2, weight=400, anchor='start'):
    """Text with subscripts. parts = list of (string, is_sub)."""
    inner = ''
    for s, sub in parts:
        if sub:
            inner += f'<tspan baseline-shift="sub" font-size="{size * FS * 0.75:.1f}">{esc(s)}</tspan>'
        else:
            inner += f'<tspan>{esc(s)}</tspan>'
    f.add(f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size * FS:.1f}" font-weight="{weight}" fill="{fill}" '
          f'text-anchor="{anchor}">{inner}</text>')


def polyline(pts):
    return 'M' + ' L'.join(f'{x:.1f},{y:.1f}' for x, y in pts)


def heading(f, x, y, t, size=17):
    f.text(x, y, t, size, INK, 700)


def diamond(f, x, y, s=8, color=None, fill=WHITE):
    color = color or ORANGE[2]
    f.add(f'<path d="M{x:.1f},{y - s:.1f} L{x + s:.1f},{y:.1f} L{x:.1f},{y + s:.1f} L{x - s:.1f},{y:.1f} Z" '
          f'fill="{fill}" stroke="{color}" stroke-width="2.4"/>')


# ---------------------------------------------------------------------------
# Figure 1: the mean keeps improving while the tail turns back (illustrative)
# ---------------------------------------------------------------------------
def concept():
    f = Fig(1200, 560, 'Mean improves while the tail turns back',
            'Illustrative curves of error change since generation 0 for a loop that keeps edits that lower mean '
            'error. Mean error falls steadily. Tail error, for the StaBLE fall-risk group, falls for about eight '
            'generations, stops gaining, then rises and passes its starting value near generation 24.')
    heading(f, 60, 58, 'The mean keeps improving while the tail turns back')
    f.pill(1000, 36, 'illustrative', 'slate', size=13)
    x0, x1, y0, y1 = 150, 900, 110, 470
    ymin, ymax = -0.07, 0.03

    def X(t):
        return x0 + (x1 - x0) * t / 50

    def Y(v):
        return y1 - (y1 - y0) * (v - ymin) / (ymax - ymin)

    def mean_fn(t):
        return -0.06 * (1 - math.exp(-t / 14))

    def tail_fn(t):
        return -0.0045 * t * math.exp(-t / 10) + 0.0004 * t

    # axes
    f.line(x0, y1, x1, y1, SLATE[0], 1.6)
    f.line(x0, y0, x0, y1, SLATE[0], 1.6)
    for t in range(0, 51, 10):
        f.line(X(t), y1, X(t), y1 + 6, SLATE[0], 1.4)
        f.text(X(t), y1 + 26, str(t), 13, MUTED, 400, 'middle')
    f.text((x0 + x1) / 2, y1 + 56, 'generation of the self-improvement loop', 14, INK2, 400, 'middle')
    f.line(x0, Y(0), x1, Y(0), SLATE[0], 1.4, dash='6 6')
    f.text(x0 - 12, Y(0) + 5, 'start', 14, MUTED, 400, 'end')
    f.text(x0 - 12, y0 + 10, 'worse', 14, MUTED, 400, 'end')
    f.text(x0 - 12, y1 - 4, 'better', 14, MUTED, 400, 'end')
    f.text(x0 + 10, y0 - 14, 'error change since generation 0', 14, INK2, 400)

    ts = [i * 0.5 for i in range(101)]
    f.path(polyline([(X(t), Y(mean_fn(t))) for t in ts]), stroke=BLUE[0], sw=3.2)
    f.path(polyline([(X(t), Y(tail_fn(t))) for t in ts]), stroke=ORANGE[0], sw=3.2)
    f.text(x1 + 16, Y(mean_fn(50)) + 5, 'mean error', 15, BLUE[2], 700)
    f.text(x1 + 16, Y(tail_fn(50)) - 2, 'tail error', 15, ORANGE[2], 700)
    f.text(x1 + 16, Y(tail_fn(50)) + 20, '(StaBLE fall-risk group)', 13, ORANGE[2], 400)

    # the true minimum of the tail curve
    tmin = min((i * 0.01 for i in range(1, 3000)), key=tail_fn)
    mx, my = X(tmin), Y(tail_fn(tmin))
    f.line(mx, my - 9, mx, Y(0) - 10, ORANGE[0], 1.4)
    f.circle(mx, my, 5.5, fill=ORANGE[0], stroke=WHITE, sw=1.4)
    f.text(mx, Y(0) - 18, 'tail stops gaining', 13, ORANGE[2], 600, 'middle')
    # where the tail passes its start
    tc = next(i * 0.01 for i in range(500, 5000) if tail_fn(i * 0.01) > 0)
    cx = X(tc)
    f.circle(cx, Y(0), 5.5, fill=ORANGE[0], stroke=WHITE, sw=1.4)
    f.text(cx + 14, Y(0) + 26, 'back above its start', 13, ORANGE[2], 600)
    f.save(os.path.join(OUT, 'concept-mean-vs-tail.svg'))


# ---------------------------------------------------------------------------
# Figure 2: edit-effect scatter and the mean rule's acceptance line
# ---------------------------------------------------------------------------
def scatter():
    f = Fig(1220, 670, 'Accepted edits that harm the tail',
            'Illustrative scatter of candidate edits by estimated majority gain and estimated tail gain, drawn with '
            'a correlation of minus 0.4. The mean rule with tail weight 0.125 accepts edits to the right of a nearly '
            'vertical line. Accepted edits below zero tail gain are orange and lie in a shaded region labelled '
            'accepted, tail harmed.')
    heading(f, 60, 46, 'The mean rule accepts many edits that harm the tail')
    f.pill(1060, 26, 'illustrative', 'slate', size=13)
    x0, x1, y0, y1 = 150, 720, 110, 600
    lo, hi = -3.0, 3.0

    def X(a):
        return x0 + (x1 - x0) * (a - lo) / (hi - lo)

    def Y(b):
        return y1 - (y1 - y0) * (b - lo) / (hi - lo)

    pi = 0.125
    slope = -(1 - pi) / pi  # b = slope * a on the acceptance line
    a_at_bottom = lo / slope
    a_top = hi / slope
    poly = [(X(0), Y(0)), (X(a_at_bottom), Y(lo)), (X(hi), Y(lo)), (X(hi), Y(0))]
    f.add(f'<path d="{polyline(poly)} Z" fill="{ORANGE[1]}" stroke="none"/>')
    f.rect(x0, y0, x1 - x0, y1 - y0, fill='none', stroke=RULE, rx=0, sw=1.4)
    f.line(x0, Y(0), x1, Y(0), SLATE[0], 1.2, dash='4 5')
    f.line(X(0), y0, X(0), y1, RULE, 1.2, dash='4 5')
    lx0, ly0, lx1, ly1 = X(a_top), Y(hi), X(a_at_bottom), Y(lo)
    f.line(lx0, ly0, lx1, ly1, BLUE[0], 2.6)

    # in-plot labels, kept clear of points
    labels = [
        (X(a_top) - 14, y0 + 30, 'rejected', SLATE[2], 'end'),
        (X(0) + 14, y0 + 30, 'accepted', BLUE[2], 'start'),
        (X(1.85), Y(-2.55), 'accepted, tail harmed', ORANGE[2], 'middle'),
    ]
    boxes = []
    for x, y, t, col, anc in labels:
        w = tw(t, 14, 700)
        bx0 = x - w if anc == 'end' else (x - w / 2 if anc == 'middle' else x)
        boxes.append((bx0 - 12, y - 24, bx0 + w + 12, y + 12))

    def dist_to_line(px, py):
        dx, dy = lx1 - lx0, ly1 - ly0
        return abs(dy * (px - lx0) - dx * (py - ly0)) / math.hypot(dx, dy)

    rng = random.Random(6)
    rho = -0.4
    pts = []
    tries = 0
    while len(pts) < 76 and tries < 20000:
        tries += 1
        z1, z2 = rng.gauss(0, 1), rng.gauss(0, 1)
        a = -0.15 + 1.0 * z1
        b = -0.15 + 1.0 * (rho * z1 + math.sqrt(1 - rho ** 2) * z2)
        if not (lo + 0.18 < a < hi - 0.18 and lo + 0.18 < b < hi - 0.18):
            continue
        px, py = X(a), Y(b)
        if dist_to_line(px, py) < 15 or abs(py - Y(0)) < 10:
            continue
        if any(bx0 <= px <= bx1 and by0 <= py <= by1 for bx0, by0, bx1, by1 in boxes):
            continue
        if any(math.hypot(px - qx, py - qy) < 15 for qx, qy, _, _ in pts):
            continue
        pts.append((px, py, a, b))
    for px, py, a, b in pts:
        acc = (1 - pi) * a + pi * b > 0
        if not acc:
            f.circle(px, py, 5.5, fill=WHITE, stroke=SLATE[0], sw=1.6)
        elif b < 0:
            f.circle(px, py, 6, fill=ORANGE[0], stroke=WHITE, sw=1.2)
        else:
            f.circle(px, py, 6, fill=BLUE[0], stroke=WHITE, sw=1.2)
    for x, y, t, col, anc in labels:
        f.text(x, y, t, 14, col, 700, anc)

    f.text((x0 + x1) / 2, y1 + 40, 'estimated majority gain of the edit', 14, INK2, 400, 'middle')
    f.text(x0, y0 - 18, 'estimated tail gain of the edit', 14, INK2, 400)
    f.text(x0 - 10, Y(0) + 5, '0', 13, MUTED, 400, 'end')
    f.text(X(0), y1 + 18, '0', 13, MUTED, 400, 'middle')

    # legend on the right
    lx, ly = 790, 170
    f.text(lx, ly - 52, 'tail weight π = 0.125; edits drawn with ρ = −0.4', 14, MUTED)
    f.line(lx, ly, lx + 40, ly, BLUE[0], 2.6)
    f.text(lx + 54, ly + 5, 'acceptance line (score S = 0)', 14, INK2)
    f.circle(lx + 20, ly + 40, 6, fill=BLUE[0], stroke=WHITE, sw=1.2)
    f.text(lx + 54, ly + 45, 'accepted, tail gains', 14, INK2)
    f.circle(lx + 20, ly + 78, 6, fill=ORANGE[0], stroke=WHITE, sw=1.2)
    f.text(lx + 54, ly + 83, 'accepted, tail harmed', 14, INK2)
    f.circle(lx + 20, ly + 116, 5.5, fill=WHITE, stroke=SLATE[0], sw=1.6)
    f.text(lx + 54, ly + 121, 'rejected', 14, INK2)
    f.save(os.path.join(OUT, 'edit-effect-scatter.svg'))


# ---------------------------------------------------------------------------
# Figure 3: where selection on the mean lowers the tail (computed from the formula)
# ---------------------------------------------------------------------------
def sign_map():
    f = Fig(1220, 620, 'Correlation threshold below which mean selection lowers the tail',
            'Threshold correlation rho star equals minus pi times sigma b over one minus pi times sigma a, plotted '
            'against the tail share pi for three ratios of tail to majority spread. Below a curve the selection '
            'term lowers the tail for that spread ratio; above all three it raises the tail. Evaluation noise does '
            'not move the curves. At a tail share of 0.125 the thresholds are minus 0.143, minus 0.286 and minus '
            '0.571.')
    f.pill(972, 30, 'computed from the formula', 'slate', size=13)
    x0, x1, y0, y1 = 150, 760, 90, 550
    pmax = 0.5

    def X(p):
        return x0 + (x1 - x0) * p / pmax

    def Y(r):
        return y1 - (y1 - y0) * (r + 1) / 2

    ratios = [(1, None, '1 × majority'), (2, '9 6', '2 × majority'), (4, '2 6', '4 × majority')]
    ps = [i * pmax / 200 for i in range(201)]
    f.rect(x0, y0, x1 - x0, y1 - y0, fill='none', stroke=RULE, rx=0, sw=1.4)
    for r in (-1, -0.5, 0, 0.5, 1):
        f.text(x0 - 12, Y(r) + 5, f'{r:+.1f}'.replace('+0.0', '0').replace('-', '−'), 13, MUTED, 400, 'end')
        if r not in (-1, 1):
            f.line(x0, Y(r), x0 + 6, Y(r), SLATE[0], 1.2)
    for p in (0, 0.1, 0.2, 0.3, 0.4, 0.5):
        f.text(X(p), y1 + 24, f'{p:.1f}', 13, MUTED, 400, 'middle')
    f.line(x0, Y(0), x1, Y(0), SLATE[0], 1.1, dash='4 5')
    f.text((x0 + x1) / 2, y1 + 54, 'tail share of the objective, π', 14, INK2, 400, 'middle')
    f.text(x0, y0 - 18, 'correlation of majority and tail effects, ρ', 14, INK2, 400)

    for ratio, dash, *_ in ratios:
        pts = []
        for p in ps:
            v = -ratio * p / (1 - p)
            if v < -1:
                break
            pts.append((X(p), Y(v)))
        f.path(polyline(pts), stroke=ORANGE[0], sw=3, dash=dash)
    p0 = 0.125
    f.line(X(p0), y0 + 4, X(p0), y1, SLATE[0], 1.4, dash='6 5')
    for ratio, *_ in ratios:
        v = -ratio * p0 / (1 - p0)
        f.circle(X(p0), Y(v), 6, fill=WHITE, stroke=ORANGE[2], sw=2.4)
    f.text(X(p0) + 10, y0 + 24, 'π = 0.125', 13, INK2)
    f.text(X(0.30), Y(0.55), 'selection helps the tail', 15, BLUE[2], 700, 'middle')
    f.text(x0 + 10, Y(-0.79), 'selection', 13, ORANGE[2], 700)
    f.text(x0 + 10, Y(-0.79) + 20, 'harms the tail', 13, ORANGE[2], 700)

    # legend
    lx, ly = 810, 140
    f.text(lx, ly, 'Tail effect spread', 15, INK, 700)
    f.text(lx + 370, ly, 'ρ* at π = 0.125', 15, INK, 700, 'end')
    for i, (ratio, dash, lab) in enumerate(ratios):
        yy = ly + 38 + i * 36
        f.path(f'M{lx:.1f},{yy - 5:.1f} L{lx + 46:.1f},{yy - 5:.1f}', stroke=ORANGE[0], sw=3, dash=dash)
        f.text(lx + 60, yy, lab, 14, INK2)
        v = -ratio * p0 / (1 - p0)
        f.text(lx + 370, yy, f'{v:.3f}'.replace('-', '−'), 14, ORANGE[2], 600, 'end')
    f.text(lx, ly + 176, 'Each curve is where the selection', 14, INK2)
    f.text(lx, ly + 198, 'term is zero. Below a curve, selection', 14, INK2)
    f.text(lx, ly + 220, 'harms the tail for that spread ratio.', 14, INK2)
    f.save(os.path.join(OUT, 'drift-sign-map.svg'))


# ---------------------------------------------------------------------------
# Figure 4: three timing regimes from the geometric model (schematic)
# ---------------------------------------------------------------------------
def regimes():
    f = Fig(1260, 600, 'Where the seed harness sits decides when the tail starts to lose',
            'Schematic of the geometric model. The tail optimum and the mean optimum are joined by the diameter of '
            'a ball; inside it, to leading order in step size, the expected tail gain under selection on the mean is negative. Three seed harnesses '
            'move toward the mean optimum. Seed 1 on the majority side stays outside the ball and the tail gains '
            'throughout. Seed 2 beyond the tail optimum enters the ball at a marked point, which is where its tail '
            'curve peaks. Seed 3 starts inside and the tail loses from the start.')
    f.pill(60, 30, 'schematic', 'slate', size=13)
    cy = 340
    xb, xa = 250, 700
    xw = xa - 0.2 * (xa - xb)
    cx, r = (xb + xw) / 2, (xw - xb) / 2
    f.add(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}" fill="{ORANGE[1]}" stroke="{ORANGE[0]}" '
          f'stroke-width="1.8" stroke-dasharray="7 6"/>')
    f.text(cx, cy - r - 18, 'inside the ball, expected tail gain per generation is negative (leading order)', 14, ORANGE[2], 600, 'middle')
    f.line(xb, cy, xa, cy, RULE, 1.4)

    seeds = [((800, 440), '1'), ((130, 250), '2'), ((520, 210), '3')]
    entry = None
    for (sx, sy), lab in seeds:
        dx, dy = xw - sx, cy - sy
        d = math.hypot(dx, dy)
        ux, uy = dx / d, dy / d
        bx, by = sx + ux * 18, sy + uy * 18
        ex, ey = xw - ux * 12, cy - uy * 12
        mx, my = sx + ux * d * 0.62, sy + uy * d * 0.62
        f.line(bx, by, ex, ey, SLATE[0], 2, dash='7 5')
        hx, hy, L, W = mx + ux * 9, my + uy * 9, 18, 8
        f.add(f'<path d="M{hx:.1f},{hy:.1f} L{hx - ux * L - uy * W:.1f},{hy - uy * L + ux * W:.1f} '
              f'L{hx - ux * L + uy * W:.1f},{hy - uy * L - ux * W:.1f} Z" fill="{SLATE[0]}"/>')
        f.circle(sx, sy, 15, fill=WHITE, stroke=SLATE[0], sw=2)
        f.text(sx, sy + 6, lab, 15, INK, 700, 'middle')
        if lab == '2':
            # first point of the path inside the ball
            t = next(i / 1000 for i in range(1000) if math.hypot(sx + dx * i / 1000 - cx, sy + dy * i / 1000 - cy) < r)
            entry = (sx + dx * t, sy + dy * t)
    diamond(f, entry[0], entry[1], 8)

    for x, col in [(xb, ORANGE), (xw, BLUE), (xa, BLUE)]:
        f.circle(x, cy, 8, fill=col[0], stroke=WHITE, sw=1.5)
    f.text(xb - 14, cy + 5, 'tail optimum', 13, ORANGE[2], 600, 'end')
    f.text(xw - 10, cy + 32, 'mean optimum', 13, BLUE[2], 600, 'end')
    f.text(xa + 4, cy - 18, 'majority optimum', 13, BLUE[2], 600, 'middle')

    f.text(800, 484, 'stays outside', 14, INK2, 600, 'middle')
    f.text(130, 222, 'enters the ball', 14, INK2, 600, 'middle')
    f.text(496, 216, 'starts inside', 14, INK2, 600, 'end')

    # right: tail gain since start, per regime
    px, pw, ph = 900, 300, 104
    tops = [92, 252, 412]
    titles = ['1  stays outside: gain', '2  enters the ball: inverted U', '3  starts inside: decline']
    curves = [lambda t: 1 - math.exp(-3 * t),
              lambda t: 4.2 * t * math.exp(1 - 4.2 * t) * 0.9 - 0.25 * t,
              lambda t: -(1 - math.exp(-2.5 * t))]
    for k, (top, title, fn) in enumerate(zip(tops, titles, curves)):
        f.text(px, top - 12, title, 14, INK, 700)
        base = top + ph / 2
        f.line(px, top, px, top + ph, SLATE[0], 1.3)
        f.line(px, base, px + pw, base, SLATE[0], 1.1, dash='4 5')
        f.text(px - 8, base + 5, '0', 13, MUTED, 400, 'end')
        pts = [(px + pw * t, base - fn(t) * ph * 0.42) for t in [i / 80 for i in range(81)]]
        f.path(polyline(pts), stroke=ORANGE[0], sw=3)
        if k == 1:
            tpk = max((i / 1000 for i in range(1, 1000)), key=fn)
            diamond(f, px + pw * tpk, base - fn(tpk) * ph * 0.42, 7)
    f.text(px + pw, tops[-1] + ph + 26, 'generation', 13, MUTED, 400, 'end')
    f.text(px, 46, 'cumulative tail gain since the seed', 14, INK2, 600)
    f.save(os.path.join(OUT, 'timing-regimes-geometry.svg'))


# ---------------------------------------------------------------------------
# Figure 6 in the text: the instrumented loop
# ---------------------------------------------------------------------------
def loop():
    f = Fig(1300, 680, 'Every candidate is scored on hidden guard people',
            'Flowchart. A parent harness goes to a proposer that writes K candidate edits per generation. Dev people '
            'score each candidate and the gate keeps the best if its score passes the threshold; the kept edit becomes '
            'the next parent. All K candidates are also scored on guard people, who are hidden from the proposer and '
            'the gate. The guard log pairs each candidate tail effect on guard people with the keep or reject decision. '
            'Saved checkpoints go to sealed test people. A forecast fitted on generations 0 to 10 and frozen at '
            'generation 10 is compared with the tail change they measure at generation 50.')
    bw, bh = 250, 108
    A = (40, 120)
    B = (355, 120)
    Cc = (670, 120)
    f.card(A[0], A[1], bw, bh, 'blue', title='Parent harness', body='prompts, tools, code')
    f.card(B[0], B[1], bw, bh, 'blue', title='Proposer', body='writes K candidate edits per generation')
    f.card(Cc[0], Cc[1], bw, bh, 'blue', title='Gate on dev people', body='score S; keep the best candidate if S > τ')
    f.arrow([(A[0] + bw + 4, A[1] + bh / 2), (B[0] - 6, B[1] + bh / 2)], color=SLATE[0], sw=2)
    f.arrow([(B[0] + bw + 4, B[1] + bh / 2), (Cc[0] - 6, Cc[1] + bh / 2)], color=SLATE[0], sw=2)
    f.arrow([(Cc[0] + bw / 2, Cc[1] - 4), (Cc[0] + bw / 2, 66), (A[0] + bw / 2, 66), (A[0] + bw / 2, A[1] - 6)],
            color=BLUE[0], sw=2.2)
    f.text((A[0] + Cc[0] + bw) / 2, 54, 'the kept edit, if any, becomes the next parent', 14, BLUE[2], 600, 'middle')

    # row 2: guard and drift log
    E = (670, 320)
    F = (1040, 320)
    fw = 220
    f.card(E[0], E[1], bw, bh, 'slate', title='Guard people', body='score every candidate; never shown to the loop')
    f.card(F[0], F[1], fw, bh, 'orange', title='Guard log', body="pairs each candidate's tail effect with its gate decision")
    f.arrow([(B[0] + bw / 2, B[1] + bh + 4), (B[0] + bw / 2, E[1] + bh / 2), (E[0] - 6, E[1] + bh / 2)],
            color=SLATE[0], sw=2)
    f.text(B[0] + bw / 2 + 14, E[1] + bh / 2 - 12, 'all K candidates', 13, INK2)
    f.arrow([(E[0] + bw + 4, E[1] + bh / 2), (F[0] - 6, F[1] + bh / 2)], color=SLATE[0], sw=2)
    f.text((E[0] + bw + F[0]) / 2, E[1] + bh / 2 - 12, 'tail effect', 13, INK2, 600, 'middle')
    fx = F[0] + fw / 2
    f.arrow([(Cc[0] + bw + 4, Cc[1] + bh / 2), (fx, Cc[1] + bh / 2), (fx, F[1] - 6)], color=BLUE[0], sw=2)
    f.text(fx - 12, (Cc[1] + bh + F[1]) / 2 + 10, 'decision for each candidate', 13, BLUE[2], 600, 'end')

    # row 3: forecast, sealed test and the comparison
    G = (1040, 530)
    H = (410, 530)
    hw = 300
    gh = 124
    f.card(G[0], G[1], fw, gh, 'orange', title='Forecast', body='tail change from generation 0 to 50, frozen at generation 10')
    f.card(H[0], H[1], hw, gh, 'aqua', title='Sealed test people', body='opened after the run: tail change from generation 0 to 50')
    f.arrow([(A[0] + bw / 2, A[1] + bh + 4), (A[0] + bw / 2, H[1] + gh / 2), (H[0] - 6, H[1] + gh / 2)],
            color=SLATE[0], sw=2)
    f.text(A[0] + bw / 2 + 12, (A[1] + bh + H[1] + gh / 2) / 2, 'saved checkpoints', 13, INK2)
    f.arrow([(fx, F[1] + bh + 4), (fx, G[1] - 6)], color=ORANGE[0], sw=2)
    f.text(fx - 12, (F[1] + bh + G[1]) / 2 + 6, 'fit on generations 0 to 10', 13, ORANGE[2], 400, 'end')
    nx, ny, nw, nh = 795, 530 + gh / 2 - 28, 150, 56
    f.rect(nx, ny, nw, nh, fill=WHITE, stroke=SLATE[0], rx=28, sw=1.8)
    f.text(nx + nw / 2, ny + nh / 2 + 6, 'compare', 15, INK, 700, 'middle')
    f.arrow([(G[0] - 4, ny + nh / 2), (nx + nw + 6, ny + nh / 2)], color=ORANGE[0], sw=2)
    f.arrow([(H[0] + hw + 4, ny + nh / 2), (nx - 6, ny + nh / 2)], color=AQUA[0], sw=2)
    f.lock(H[0] + hw - 34, H[1] + 14, 1.1, color=AQUA[2])
    f.lock(E[0] + bw - 34, E[1] + 14, 1.1, color=SLATE[2])
    f.save(os.path.join(OUT, 'instrumented-loop.svg'))


# ---------------------------------------------------------------------------
# Figure 7 in the text: person-level splits in StaBLE
# ---------------------------------------------------------------------------
def splits():
    f = Fig(1260, 520, 'Each person is dev, guard or test, and test exactly once',
            'StaBLE person-level folds. Grid of five outer folds by five blocks of about 34 people, stratified by '
            'fall-risk group and age. In each fold one block is sealed test people, the next block is guard people, and the '
            'other three blocks are dev people.')
    heading(f, 60, 46, 'StaBLE folds, split by person')
    f.text(60, 74, '171 people in five blocks of about 34, stratified by fall-risk group and age; each block is sealed test once', 14, INK2)
    gx, gy, cw, ch, gap = 170, 140, 136, 54, 10
    roles = {'dev': BLUE, 'guard': SLATE, 'sealed test': AQUA}
    for j in range(5):
        f.text(gx + j * (cw + gap) + cw / 2, gy - 16, f'block {j + 1}', 13, MUTED, 400, 'middle')
    for i in range(5):
        y = gy + i * (ch + gap)
        f.text(gx - 16, y + ch / 2 + 5, f'outer fold {i + 1}', 14, INK2, 400, 'end')
        for j in range(5):
            role = 'sealed test' if j == i else ('guard' if j == (i + 1) % 5 else 'dev')
            col = roles[role]
            x = gx + j * (cw + gap)
            f.rect(x, y, cw, ch, fill=col[1], stroke=col[0], rx=8, sw=1.6 if role != 'sealed test' else 2.2)
            f.text(x + cw / 2, y + ch / 2 + 6, role, 15, col[2], 700 if role == 'sealed test' else 600, 'middle')
    lx = 930
    items = [('dev', BLUE, 'about 103 people per fold; the loop scores and keeps edits'),
             ('guard', SLATE, 'about 34 per fold; scores every candidate, never shown to the loop'),
             ('sealed test', AQUA, 'about 34 per fold; measures the forecast target')]
    yy = 160
    for role, col, desc in items:
        f.rect(lx, yy - 16, 22, 22, fill=col[1], stroke=col[0], rx=5, sw=1.6)
        f.text(lx + 34, yy, role, 15, INK, 700)
        yy = f.para(lx + 34, yy + 24, desc, 270, 13, INK2) + 30
    f.save(os.path.join(OUT, 'stable-person-splits.svg'))


# ---------------------------------------------------------------------------
# Figure 8 in the text: dose-response design in Global-MMLU (illustrative prediction)
# ---------------------------------------------------------------------------
def dose():
    f = Fig(1260, 560, 'Tail share sets the sign of drift; tail sample size scales it',
            'Global-MMLU design. Grid of twelve cells, tail share pi of 0.05, 0.10, 0.20 and 0.40 by tail evaluation '
            'size of 16, 64 and 256 items. Each cell shows the drift per proposal the correlated-response law predicts '
            'for an assumed correlation of minus 0.3, equal spreads and zero mean effects. Cells with pi up to 0.20 '
            'are predicted to harm the tail, cells with pi 0.40 to help it; a bracket marks the predicted sign change '
            'near pi 0.23, where the model predicts zero drift. More tail items raise the gain at pi 0.40 from 0.083 to 0.123 without changing its sign.')
    heading(f, 60, 50, 'Global-MMLU: predicted tail drift per proposal')
    f.pill(1010, 30, 'illustrative prediction', 'slate', size=13)
    pis = [0.05, 0.10, 0.20, 0.40]
    nbs = [16, 64, 256]
    rho, sa, sb, na, v = -0.3, 1.0, 1.0, 256, 64.0
    phi0 = 1 / math.sqrt(2 * math.pi)

    def drift(p, nb):
        s2a, s2b = v / na, v / nb
        cov = (1 - p) * rho * sa * sb + p * sb ** 2
        var = (1 - p) ** 2 * (sa ** 2 + s2a) + p ** 2 * (sb ** 2 + s2b) + 2 * p * (1 - p) * rho * sa * sb
        return cov / math.sqrt(var) * phi0

    gx, gy, cw, ch, gap = 250, 150, 150, 92, 10
    for j, p in enumerate(pis):
        f.text(gx + j * (cw + gap) + cw / 2, gy - 16, f'π = {p:.2f}', 15, INK2, 600, 'middle')
    f.text(gx + 2 * (cw + gap) - gap / 2, gy - 52, 'tail share of the objective', 14, INK2, 400, 'middle')
    for i, nb in enumerate(nbs):
        y = gy + i * (ch + gap)
        f.text(gx - 16, y + ch / 2 + 5, f'{nb} tail items', 14, INK2, 400, 'end')
        for j, p in enumerate(pis):
            d = drift(p, nb)
            x = gx + j * (cw + gap)
            col = ORANGE if d < 0 else BLUE
            op = min(1.0, 0.25 + abs(d) / 0.13 * 0.75)
            f.rect(x, y, cw, ch, fill=col[1], stroke=col[0], rx=8, sw=1.4)
            f.add(f'<rect x="{x + 1:.1f}" y="{y + 1:.1f}" width="{cw - 2:.1f}" height="{ch - 2:.1f}" rx="7" '
                  f'fill="{col[0]}" opacity="{op * 0.35:.2f}"/>')
            f.text(x + cw / 2, y + ch / 2 - 4, ('harm' if d < 0 else 'gain'), 15, col[2], 700, 'middle')
            f.text(x + cw / 2, y + ch / 2 + 20, f'{d:+.3f}'.replace('-', '−'), 14, col[2], 400, 'middle')
    gb = gy + 3 * (ch + gap) - gap
    # bracket between the 0.20 and 0.40 columns
    c3, c4 = gx + 2 * (cw + gap) + cw / 2, gx + 3 * (cw + gap) + cw / 2
    f.path(f'M{c3:.1f},{gb + 10:.1f} L{c3:.1f},{gb + 22:.1f} L{c4:.1f},{gb + 22:.1f} L{c4:.1f},{gb + 10:.1f}',
           stroke=INK2, sw=2)
    f.text((c3 + c4) / 2, gb + 50, 'model predicts zero drift near π = 0.23', 14, INK, 600, 'middle')
    f.text(gx, gb + 86, 'cells: drift per proposal, in units of the majority spread', 13, MUTED)
    # callout: more tail items change the size, not the sign
    ax = gx + 4 * (cw + gap) + 14
    f.arrow([(ax, gy + ch / 2), (ax, gy + 2 * (ch + gap) + ch / 2)], color=BLUE[0], sw=2)
    f.text(ax + 16, gy + ch + 18, 'at π = 0.40,', 14, INK2, 400)
    f.text(ax + 16, gy + ch + 40, 'more tail items:', 14, INK2, 400)
    f.text(ax + 16, gy + ch + 62, '+0.083 → +0.123,', 14, BLUE[2], 600)
    f.text(ax + 16, gy + ch + 84, 'same sign', 14, INK2, 400)
    f.save(os.path.join(OUT, 'dose-response-design.svg'))


# ---------------------------------------------------------------------------
# Figure 5 in the text: validity and price of tail protection (preliminary simulation)
# ---------------------------------------------------------------------------
def guarantee():
    f = Fig(1300, 600, 'Only fresh or sealed tail data keep the guarantee, and protection gets cheaper with more tail people',
            'Left: with edits pushing against the margin and normal per-person noise, observed rate at which a '
            'protected harness breaches the tail margin (is more than the margin worse than the seed on the tail), for four designs; each bar spans '
            '5 to 20 tail people per test, log scale, with the nominal 0.05 marked. For the gates the event is any '
            'accepted parent; for certification it is the deployed checkpoint. Per-step testing against the parent '
            'and reuse of the same tail people exceed the nominal level; fresh people and checkpoint certification '
            'stay below it. Right: with tail-neutral edits, share of the unprotected loop majority gain kept against '
            'tail people per test, rising from 9 to 57 percent for fresh gating and 15 to 42 percent for '
            'certification, against 97 percent for an oracle.')
    f.pill(1060, 14, 'preliminary simulation', 'slate', size=13)
    # left panel
    heading(f, 50, 66, 'How often is the tail margin breached?', 16)
    f.text(50, 96, 'each bar: range over 5 to 20 tail people per test', 14, MUTED)
    x0, x1 = 330, 640
    lmin, lmax = -4, 0

    def X(p):
        return x0 + (x1 - x0) * (math.log10(p) - lmin) / (lmax - lmin)

    rows = [('per-step gate vs parent', 1.0, 1.0, ORANGE, 'any accepted parent'),
            ('cumulative, reused people', 0.11, 0.29, ORANGE, 'any accepted parent'),
            ('checkpoint certification', 0.016, 0.019, AQUA, 'deployed checkpoint only'),
            ('cumulative, fresh people', 0.0003, 0.0013, AQUA, 'any accepted parent')]
    ty, rh = 176, 72
    yb = ty + len(rows) * rh
    f.line(x0, yb - 10, x1, yb - 10, SLATE[0], 1.4)
    for k, lab in [(-4, '0.0001'), (-3, '0.001'), (-2, '0.01'), (-1, '0.1'), (0, '1')]:
        xx = x0 + (x1 - x0) * (k - lmin) / (lmax - lmin)
        f.line(xx, yb - 10, xx, yb - 4, SLATE[0], 1.3)
        f.text(xx, yb + 14, lab, 13, MUTED, 400, 'middle')
    f.text((x0 + x1) / 2 - 40, yb + 44, 'observed rate of breaching the tail margin M (log scale)', 14, INK2, 400, 'middle')
    xn = X(0.05)
    f.line(xn, ty - 26, xn, yb - 10, INK2, 1.8, dash='6 5')
    f.text(xn, ty - 34, 'nominal 0.05', 13, INK, 600, 'middle')
    for i, (lab, lo, hi, col, event) in enumerate(rows):
        y = ty + i * rh + 20
        f.text(x0 - 22, y + 2, lab, 14, INK2, 400, 'end')
        f.text(x0 - 22, y + 22, 'breach: ' + event, 13, MUTED, 400, 'end')
        if hi / lo > 1.05:
            f.line(X(lo), y, X(hi), y, col[0], 9, cap='round')
        else:
            f.circle(X(lo), y, 6.5, fill=col[0], stroke=col[0], sw=1)
            f.text(X(lo), y + 26, '1.0 at every size', 13, ORANGE[2], 600, 'middle')

    # right panel
    heading(f, 760, 66, 'How much majority gain is kept?', 16)
    f.text(760, 94, "tail-neutral edits; share of the unprotected loop's gain", 13, MUTED)
    px0, px1, py0, py1 = 800, 1120, 150, 440
    ns = [5, 10, 20]

    def PX(n):
        # a small pad keeps the first, dodged markers clear of the y axis
        return px0 + 18 + (px1 - px0 - 18) * (n - 5) / 15  # pad keeps markers off the y axis

    def PY(v):
        return py1 - (py1 - py0) * v / 100

    f.line(px0, py1, px1 + 16, py1, SLATE[0], 1.4)
    f.line(px0, py0, px0, py1, SLATE[0], 1.4)
    for v in (0, 50, 100):
        f.text(px0 - 10, PY(v) + 5, f'{v}%', 13, MUTED, 400, 'end')
        f.line(px0 - 5, PY(v), px0, PY(v), SLATE[0], 1.3)
    for n in ns:
        f.line(PX(n), py1, PX(n), py1 + 6, SLATE[0], 1.3)
        f.text(PX(n), py1 + 24, str(n), 13, MUTED, 400, 'middle')
    f.text((px0 + px1) / 2, py1 + 54, 'tail people per test', 14, INK2, 400, 'middle')
    # certification is drawn first so the filled fresh-people dots stay visible where the series meet
    # the two green series are dodged 6 px apart so their markers stay separate where they meet
    # both green series sit on the true sample sizes; the large open square stays visible around the small dot
    series = [('oracle', [96.9, 96.9, 96.9], SLATE, '2 6', 'circle', 0),
              ('certification', [14.6, 29.1, 42.2], AQUA, '9 6', 'square', 0),
              ('fresh people', [9.0, 31.0, 56.8], AQUA, None, 'dot', 0)]
    for lab, vals, col, dash, shape, dodge in series:
        pts = [(PX(n) + dodge, PY(v)) for n, v in zip(ns, vals)]
        f.path(polyline(pts), stroke=col[0], sw=3, dash=dash)
        for x, y in pts:
            if shape == 'square':
                f.rect(x - 8, y - 8, 16, 16, fill=WHITE, stroke=col[2], rx=1.5, sw=2.2)
            elif shape == 'dot':
                f.circle(x, y, 4.5, fill=col[0], stroke=WHITE, sw=1.2)
            else:
                f.circle(x, y, 4.5, fill=WHITE, stroke=col[0], sw=2)
    f.text(px1 + 26, PY(96.9) + 5, 'oracle, 97%', 14, SLATE[2], 600)
    f.text(px1 + 26, PY(56.8) + 5, 'fresh people', 14, AQUA[2], 600)
    f.text(px1 + 26, PY(42.2) + 5, 'certification', 14, AQUA[2], 600)
    f.save(os.path.join(OUT, 'guarantee-validity-and-price.svg'))


if __name__ == '__main__':
    concept()
    scatter()
    sign_map()
    regimes()
    loop()
    splits()
    dose()
    guarantee()
    print('ok')
