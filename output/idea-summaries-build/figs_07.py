"""Figures for proposal 07 (how a VLM agent should look at its own tool outputs).

Run: python3 -B output/idea-summaries-build/figs_07.py
Writes SVGs to docs/idea-summaries/images/07/.

Color meaning, shared by every figure:
  slate  = neutral scaffolding and raw tool output
  orange = the renderer or encoding (the thing being optimized), and what it loses or computes
  blue   = the source reader A (the VLM the search is scored against)
  aqua   = held-out readers (other VLMs, people) and the gain they share
  red    = sealed data, reader-specific exploitation, failure
"""
import math
import os
import random
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from svglib import Fig, C, FS, INK, INK2, MUTED, RULE, WHITE, MONO  # noqa: E402

OUT = os.path.normpath(os.path.join(HERE, '..', '..', 'docs', 'idea-summaries', 'images', '07'))
os.makedirs(OUT, exist_ok=True)

BL, BLF, BLD = C['blue']
OR, ORF, ORD = C['orange']
AQ, AQF, AQD = C['aqua']
RD, RDF, RDD = C['red']
SL, SLF, SLD = C['slate']


def title(f, t, sub=None):
    f.text(40, 50, t, 20, INK, 700)
    if sub:
        f.text(40, 80, sub, 14, MUTED)


def sway(n, seed, amp=1.0, drift=0.0):
    rnd = random.Random(seed)
    ph = [rnd.uniform(0, 6.28) for _ in range(6)]
    fr = [0.9, 1.7, 2.9, 4.3, 6.1, 8.7]
    wt = [1.0, 0.6, 0.45, 0.3, 0.2, 0.12]
    out = []
    for i in range(n):
        t = i / (n - 1)
        v = sum(w * math.sin(2 * math.pi * fq * t * 3 + p) for w, fq, p in zip(wt, fr, ph))
        out.append(amp * v / 2.2 + drift * (t - 0.5))
    return out


def polyline(pts):
    return 'M' + ' L'.join(f'{x:.1f},{y:.1f}' for x, y in pts)


def sub_text(f, x, y, base, sub, tail, size=16, fill=INK, weight=700, anchor='middle', sub_scale=0.72):
    """Text with a subscript, e.g. R_pi(e)."""
    f.add(f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size * FS:.1f}" font-weight="{weight}" fill="{fill}" '
          f'text-anchor="{anchor}">{base}<tspan baseline-shift="sub" font-size="{size * sub_scale * FS:.1f}">'
          f'{sub}</tspan>{tail}</text>')


def stabilogram_data():
    """Illustrative CoM path in arbitrary units, its 95% prediction ellipse and summary numbers."""
    s1, s2 = sway(160, 5, 1.0), sway(160, 9, 0.6)
    n = len(s1)
    mx, my = sum(s1) / n, sum(s2) / n
    sxx = sum((a - mx) ** 2 for a in s1) / (n - 1)
    syy = sum((b - my) ** 2 for b in s2) / (n - 1)
    sxy = sum((a - mx) * (b - my) for a, b in zip(s1, s2)) / (n - 1)
    tr, det = sxx + syy, sxx * syy - sxy ** 2
    l1 = tr / 2 + math.sqrt(tr * tr / 4 - det)
    l2 = tr / 2 - math.sqrt(tr * tr / 4 - det)
    a, b = math.sqrt(5.991 * l1), math.sqrt(5.991 * l2)  # 95% semi-axes, chi-square with 2 dof
    ang = math.degrees(0.5 * math.atan2(2 * sxy, sxx - syy))
    cm = math.sqrt(6.2 / (math.pi * a * b))  # cm per unit, chosen so the ellipse area is 6.2 cm2
    rms = math.sqrt(sxx + syy) * cm
    path = sum(math.hypot(x2 - x1, y2 - y1) for x1, x2, y1, y2 in zip(s1, s1[1:], s2, s2[1:])) * cm
    return s1, s2, (mx, my, a, b, ang), cm, rms, path


# ---------------------------------------------------------------------------
# Figure 1: one tool output, four encodings
# ---------------------------------------------------------------------------
def fig_encodings():
    f = Fig(1300, 700, 'One CoM path, four encodings',
            'The same 30 seconds of tandem-stance center-of-mass path shown as printed numbers, summary '
            'statistics, a default line plot and a clinical stabilogram, with token cost and what each keeps.')
    title(f, 'One CoM path, four ways to show it',
          '30 s of tandem stance, one phone at 60 fps; traces are illustrative')
    s1, s2, (emx, emy, ea, eb, eang), cm, rms, path = stabilogram_data()
    # tool output card: every row on the right is drawn from this one CoM path
    f.rect(40, 110, 300, 560, fill=SLF, stroke=SL)
    f.text(64, 146, 'Tool output', 16, INK, 700)
    f.camera(92, 250, 1.3, SLD)
    f.person(205, 190, 150, color=SLD, dots=True, dot_color=SLD)
    f.text(64, 418, 'OpenCap Monocular', 15, INK, 700)
    f.text(64, 446, 'center-of-mass path', 14, INK2)
    f.text(64, 492, '1,800 frames x 2', 14, INK2)
    f.text(64, 526, '= 3,600 numbers', 17, SLD, 700)

    rows = [
        ('Printed numbers', 'CoM path as text', '~25,000 text tokens', 'keeps all samples', 'slate'),
        ('Summary statistics', 'three CoM-path numbers', '~40 text tokens', 'loses timing', 'red'),
        ('Default line plot', 'both coordinates, autoscaled', '~600 image tokens', 'hides physical scale', 'red'),
        ('Clinical stabilogram', 'CoM path and 95% ellipse', '~600 image tokens', 'keeps scale, loses timing',
         'slate'),
    ]
    x, w, h = 420, 840, 125
    for i, (t, d, tok, info, irole) in enumerate(rows):
        y = 110 + i * 145
        f.rect(x, y, w, h, fill=ORF, stroke=OR)
        f.arrow([(340, y + h / 2), (x - 2, y + h / 2)], color=SL)
        # mini visual panel
        vx, vy, vw, vh = x + 16, y + 14, 240, 97
        f.rect(vx, vy, vw, vh, fill=WHITE, stroke=RULE, rx=6)
        if i == 0:
            for j, ln in enumerate(['f1     3.12  -1.87', 'f2     3.15  -1.90',
                                    'f3     3.19  -1.92', '... 1,797 more rows']):
                f.text(vx + 12, vy + 24 + j * 21, ln.replace(' ', '\u00a0').replace('-', '\u2212'), 13, INK2,
                       mono=True)
        elif i == 1:
            for j, ln in enumerate([f'RMS sway      {rms:.1f} cm', '95% ellipse   6.2 cm\u00b2',
                                    f'path length  {path:.0f} cm']):
                f.text(vx + 14, vy + 30 + j * 24, ln.replace(' ', '\u00a0'), 13, INK2, mono=True)
        elif i == 2:
            ax0, ax1, ay0, ay1 = vx + 14, vx + vw - 12, vy + 10, vy + vh - 26
            f.line(ax0, ay1, ax1, ay1, SL, 1.2)
            f.line(ax0, ay0, ax0, ay1, SL, 1.2)
            for k, sd in enumerate([3, 11]):
                s = sway(120, sd, 1.0)
                mid = (ay0 + ay1) / 2 + (k - 0.5) * 20
                pts = [(ax0 + 4 + (ax1 - ax0 - 34) * j / 119, mid + 12 * v) for j, v in enumerate(s)]
                f.path(polyline(pts), stroke=SLD if k == 0 else MUTED, sw=1.4, dash=None if k == 0 else '5 3')
                f.text(ax1 - 4, mid + 5, 'xy'[k], 13, SLD if k == 0 else MUTED, 700, 'end')
            f.text(ax1, ay1 + 18, 'time \u2192', 13, MUTED, 400, 'end')
        else:
            k = 62.0  # px per unit, equal on both axes
            cx, cy = vx + vw / 2 - 18, vy + vh / 2
            f.line(cx - 92, cy, cx + 92, cy, RULE, 1)
            f.line(cx, vy + 8, cx, vy + vh - 8, RULE, 1)
            pts = [(cx + k * (a - emx), cy - k * (b - emy)) for a, b in zip(s1, s2)]
            f.path(polyline(pts), stroke=SLD, sw=1.2)
            f.add(f'<ellipse cx="{cx:.1f}" cy="{cy:.1f}" rx="{k * ea:.1f}" ry="{k * eb:.1f}" '
                  f'transform="rotate({-eang:.1f} {cx:.1f} {cy:.1f})" fill="none" stroke="{OR}" '
                  f'stroke-width="2.2"/>')
            bar = k / cm  # px for 1 cm
            bx, by = vx + vw - 14 - bar, vy + vh - 12
            f.line(bx, by, bx + bar, by, INK, 2.2, cap='butt')
            f.text(bx + bar / 2, by - 7, '1 cm', 14.5, INK, 700, 'middle')
        f.text(x + 286, y + 50, t, 17, INK, 700)
        f.text(x + 286, y + 80, d, 14, INK2)
        f.pill(x + 576, y + 22, tok, 'slate', size=15)
        f.pill(x + 576, y + 72, info, irole, size=13.5)
    f.save(os.path.join(OUT, 'one-output-four-encodings.svg'))


# ---------------------------------------------------------------------------
# Figure 2: risk decomposition
# ---------------------------------------------------------------------------
def fig_decomposition():
    f = Fig(1300, 372, 'Where a reader error comes from',
            'A stacked bar splits the reader risk into the tool floor, the information term lost by the encoding, '
            'and the perceptual term, itself split into resolution (left after recalibration) and calibration '
            '(removed by recalibration).')
    title(f, "Where a reader's error comes from",
          'Risk grows from left to right; each boundary is a different decoder; widths are schematic')
    x0, y, hh = 90, 190, 60
    segs = [(0, 250, SLF, SL, 'tool floor'), (250, 510, ORF, OR, 'information loss I(r)'),
            (510, 820, '#cfe0f7', BL, 'resolution'), (820, 1060, BLF, BL, 'calibration')]
    for a, b, fill, stroke, lab in segs:
        f.rect(x0 + a, y, b - a, hh, fill=fill, stroke=stroke, rx=4, sw=1.6)
        f.text(x0 + (a + b) / 2, y + hh / 2 + 6, lab, 15, INK, 600, 'middle')
    # brace for perceptual term
    f.text(x0 + 1078, y + hh / 2 + 6, 'risk \u2192', 15, MUTED, 600)
    bx0, bx1, by = x0 + 510, x0 + 1060, y - 22
    f.path(f'M{bx0},{by + 8} V{by} H{bx1} V{by + 8}', stroke=BL, sw=2)
    sub_text(f, (bx0 + bx1) / 2, by - 16, 'perceptual term P', 'X', '(r)', 15, BLD, 700, sub_scale=0.85)
    # boundary labels
    bounds = [(0, ('0', '', ''), ''), (250, ('R(o)', '', ''), 'best raw-output decoder'),
              (510, ('R(r)', '', ''), 'best image decoder'),
              (820, ('R', 'h ∘ X', '(r)'), 'recalibrated reader'),
              (1060, ('R', 'X', '(r)'), 'VLM reader')]
    for xx, (base, sub, tail), how in bounds:
        X = x0 + xx
        f.line(X, y + hh, X, y + hh + 14, INK2, 1.6)
        if sub:
            sub_text(f, X, y + hh + 40, base, sub, tail, 16, INK, 700, sub_scale=0.85)
        else:
            f.text(X, y + hh + 40, base, 16, INK, 700, 'middle')
        if how:
            f.para(X, y + hh + 74, how, 200, 13.5, INK2, anchor='middle')
    f.save(os.path.join(OUT, 'risk-decomposition.svg'))


# ---------------------------------------------------------------------------
# Figure 3: oracle learning curve (preliminary simulation, sim/d_decomposition_results.json)
# ---------------------------------------------------------------------------
def fig_oracle():
    f = Fig(1240, 600, 'Too few oracle training renders make the estimated gap negative',
            'Preliminary simulation: oracle risk falls with training renders toward the true encoding floor; '
            'with 200 renders it lies above the position reader, so the estimated perceptual gap is negative.')
    title(f, 'Too few training renders make the estimated gap negative; enough renders recover it',
          'Preliminary simulation; gap = reader risk minus oracle risk')
    X0, X1, Y0, Y1 = 150, 860, 130, 490
    lx0, lx1 = math.log10(120), math.log10(35000)
    ly0, ly1 = math.log10(0.0035), math.log10(0.1)

    def mx(n):
        return X0 + (math.log10(n) - lx0) / (lx1 - lx0) * (X1 - X0)

    def my(r):
        return Y1 - (math.log10(r) - ly0) / (ly1 - ly0) * (Y1 - Y0)

    for r in [0.005, 0.01, 0.02, 0.05, 0.1]:
        f.line(X0, my(r), X1, my(r), '#eceef1', 1)
        f.text(X0 - 12, my(r) + 5, f'{r:g}', 13.5, INK2, 400, 'end')
    for n, lab in [(200, '200'), (1000, '1,000'), (5000, '5,000'), (20000, '20,000')]:
        f.line(mx(n), Y1, mx(n), Y1 + 6, INK2, 1.2)
        f.text(mx(n), Y1 + 28, lab, 13.5, INK2, 400, 'middle')
    f.line(X0, Y0, X0, Y1, INK2, 1.4)
    f.line(X0, Y1, X1, Y1, INK2, 1.4)
    f.text((X0 + X1) / 2, Y1 + 62, 'renders used to train the oracle (log scale)', 14, INK, 600, 'middle')
    f.text(X0, Y0 - 16, 'mean squared error, cm² (log scale)', 14, INK, 600)
    # true floor and reader
    R_reader, R_floor = 0.013668, 0.004997
    f.line(X0, my(R_floor), X1, my(R_floor), OR, 2.2, dash='7 6')
    f.line(X0, my(R_reader), X1, my(R_reader), BL, 2.6)
    pts = [(200, 0.06297), (1000, 0.01170), (5000, 0.005777), (20000, 0.005444)]
    # estimated gaps drawn as vertical spans between the reader line and the oracle point
    for gx, ya, yb in [(200, 0.06297, R_reader), (5000, R_reader, 0.005777)]:
        f.line(mx(gx), my(ya) + 8, mx(gx), my(yb) - 8, INK2, 2.0, dash='4 4')
    # true gap: reader risk minus the true floor, drawn as its own capped bracket past the last point
    tx = mx(30000)
    f.line(tx, my(R_reader), tx, my(R_floor), INK, 2.0)
    for yy in (my(R_reader), my(R_floor)):
        f.line(tx - 7, yy, tx + 7, yy, INK, 2.0)
    f.text(tx + 14, my(R_floor) - 4, 'true gap 0.0087 cm²', 14, INK, 600)
    f.path(polyline([(mx(n), my(r)) for n, r in pts]), stroke=OR, sw=2.6)
    for n, r in pts:
        f.circle(mx(n), my(r), 6, fill=WHITE, stroke=OR, sw=2.4)
    f.text(mx(200) + 22, my(0.06297) + 6, 'estimated gap −0.049 cm²', 14, RDD, 700)
    f.text(mx(5000) + 14, my(0.0086) + 6, 'estimated gap', 14, INK, 600)
    f.text(mx(5000) + 14, my(0.0086) + 26, '+0.0079 cm²', 14, INK, 600)
    # legend
    lx, ly = 900, 200
    items = [('line', OR, None, 'oracle risk'), ('line', OR, '7 6', 'true floor R(r)'),
             ('line', BL, None, 'position reader')]
    for i, (_, col, dash, lab) in enumerate(items):
        yy = ly + i * 44
        f.line(lx, yy, lx + 44, yy, col, 2.6, dash=dash)
        f.text(lx + 58, yy + 5, lab, 14.5, INK)
    f.save(os.path.join(OUT, 'oracle-learning-curve.svg'))


# ---------------------------------------------------------------------------
# Figure 4: renderer evolution loop
# ---------------------------------------------------------------------------
def fig_loop():
    f = Fig(1200, 860, 'The renderer search loop',
            'Cached tool outputs from development people feed a renderer program; frozen reader A reads the '
            'renders and produces fitness on dev-select people and error tables on dev-train people; the archive '
            'keeps elites; a text-only mutator edits parent code using the error tables. Sealed participants, '
            'held-out readers and held-out tasks are scored only after the search ends.')
    title(f, 'The renderer search loop', 'Only development people and the fitness reader enter the loop')
    bw, bh = 300, 104
    xs = [40, 450, 860]
    yt, yb = 230, 500
    f.rect(22, 204, 1156, 426, fill='none', stroke=SL, rx=14, sw=1.6, dash='7 6')
    f.rect(930, 194, 230, 22, fill=WHITE, stroke='none', rx=0, sw=0)
    f.text(1160, 210, 'Development search', 14.5, SLD, 700, 'end')
    f.card(40, 110, 700, 72, 'slate', 'Cached tool outputs',
           'RTMPose and OpenCap Monocular, development people, no labels', tsize=15, bsize=13.5)
    f.card(xs[0], yt, bw, bh, 'orange', 'Renderer program', 'plotting code; sees no labels', tsize=15, bsize=13.5)
    f.card(xs[1], yt, bw, bh, 'orange', 'Renders', 'one image per trial', tsize=15, bsize=13.5)
    f.card(xs[2], yt, bw, bh, 'blue', 'Reader A', 'frozen Qwen3-VL-8B, plus a probe on its vision features',
           tsize=15, bsize=13.5)
    f.card(xs[2], yb, bw, bh, 'blue', 'Fitness', 'error vs dev-select labels', tsize=15, bsize=13.5)
    f.card(xs[1], yb, bw, bh, 'orange', 'Archive', 'MAP-Elites grid by declared channel',
           tsize=15, bsize=13.5)
    f.card(xs[0], yb, bw, bh, 'orange', 'Text-only mutator', 'edits parent code; sees no images',
           tsize=15, bsize=13.5)
    ex, ey, ew, eh = xs[1], 368, bw, 98
    f.card(ex, ey, ew, eh, 'blue', 'Error tables', 'reader A and probe errors vs dev-train labels',
           tsize=15, bsize=13.5)
    cy_t, cy_b = yt + bh / 2, yb + bh / 2
    f.arrow([(xs[0] + 150, 182), (xs[0] + 150, yt - 2)], SL)
    f.arrow([(xs[0] + bw, cy_t), (xs[1] - 2, cy_t)], SL)
    f.arrow([(xs[1] + bw, cy_t), (xs[2] - 2, cy_t)], SL)
    # reader A to fitness (straight down, dev-select) and to error tables (down then left, dev-train)
    f.arrow([(xs[2] + 240, yt + bh), (xs[2] + 240, yb - 2)], SL)
    f.arrow([(xs[2] + 70, yt + bh), (xs[2] + 70, ey + eh / 2), (ex + ew + 2, ey + eh / 2)], SL)
    f.text(xs[2] + 80, yt + bh + 34, 'dev-train', 13.5, BLD, 600)
    f.text(xs[2] + 230, yb - 40, 'dev-select', 13.5, BLD, 600, 'end')
    f.arrow([(xs[2], cy_b), (xs[1] + bw + 2, cy_b)], SL)
    f.arrow([(xs[1], cy_b), (xs[0] + bw + 2, cy_b)], SL)
    gx = (xs[0] + bw + xs[1]) / 2
    f.text(gx, cy_b - 10, 'parent code', 13, INK2, 600, 'middle')
    # error tables to mutator (left, then down)
    f.arrow([(ex, ey + eh / 2), (xs[0] + 240, ey + eh / 2), (xs[0] + 240, yb - 2)], SL)
    # mutator to renderer program (up)
    f.arrow([(xs[0] + 80, yb), (xs[0] + 80, yt + bh + 2)], SL)
    f.text(xs[0] + 92, (yt + bh + yb) / 2 - 34, 'child code', 13, INK2, 600)
    # post-search scoring frame with a shared header that the saved renderers land on
    px, py, pw, ph = 40, 690, 1120, 148
    f.rect(px, py, pw, ph, fill=WHITE, stroke=RD, rx=14, sw=1.6, dash='7 6')
    ax = xs[1] + bw / 2
    f.text(ax, py + 30, 'After the search ends: score checkpoints', 15, RDD, 700, 'middle')
    cw, gap = 346, 20
    c0 = px + 20
    f.line(c0, py + 44, c0 + 3 * cw + 2 * gap, py + 44, RD, 1.4)
    cards = [(c0, 'red', 'Sealed test participants', 'never seen by the loop'),
             (c0 + cw + gap, 'aqua', 'Held-out readers', 'other VLMs, crowd, clinicians'),
             (c0 + 2 * (cw + gap), 'red', 'Held-out tasks', 'three StaBLE tasks, BioCV')]
    for cx, role, t, b in cards:
        f.card(cx, py + 54, cw, ph - 66, role, t, b, tsize=14.5, bsize=13.5)
    f.lock(c0 + cw - 30, py + 64, 1.0)
    f.arrow([(ax, yb + bh), (ax, py - 2)], RD, dash='6 5')
    f.text(ax + 14, 666, 'eight checkpoints per run', 14, RDD, 600)
    f.save(os.path.join(OUT, 'renderer-evolution-loop.svg'))


# ---------------------------------------------------------------------------
# Figure 5: fitness readers versus held-out readers
# ---------------------------------------------------------------------------
def fig_readers():
    f = Fig(1400, 700, 'Who sets the fitness and who only reads the result',
            'Rows are fitness conditions and columns are readers. Filled blue circles set the fitness; filled '
            'slate squares are held-out readers from a fitness reader family; open aqua circles are other '
            'families and people; an open slate diamond marks the crowd profile used inside one fitness. '
            'Shaded columns are readers that set fitness in no condition.')
    title(f, 'Who sets the fitness, and who only reads the result',
          'Every condition leaves at least one VLM family out')
    groups = [('Qwen3-VL', ['2B', '4B', '8B', '30B-A3B', '32B']), ('Gemma 3', ['4B', '12B', '27B']),
              ('InternVL3.5', ['\u22488B', 'larger']), ('Open 4', ['\u22488B']), ('Open 5', ['\u22488B ']),
              ('Closed', ['frontier']), ('People', ['crowd', 'clinicians'])]
    cols = []
    for g, sizes in groups:
        for s in sizes:
            cols.append((g, s))
    rows = [
        ('Qwen3-VL-8B alone', {'Qwen3-VL|8B'}),
        ('Gemma 3 12B alone', {'Gemma 3|12B'}),
        ('InternVL3.5 \u22488B alone', {'InternVL3.5|\u22488B'}),
        ('Qwen3-VL-4B alone', {'Qwen3-VL|4B'}),
        ('Qwen 8B + Qwen 4B', {'Qwen3-VL|8B', 'Qwen3-VL|4B'}),
        ('Qwen 8B + InternVL', {'Qwen3-VL|8B', 'InternVL3.5|\u22488B'}),
        ('Qwen 8B + Gemma 12B', {'Qwen3-VL|8B', 'Gemma 3|12B'}),
        ('Qwen 8B + InternVL + predicted-human term', {'Qwen3-VL|8B', 'InternVL3.5|\u22488B'}),
    ]
    ever = set().union(*[fit for _, fit in rows])
    # columns, with a small extra gap between reader groups
    colx, x = [], 466
    for gi, (g, sizes) in enumerate(groups):
        if gi:
            x += 10 if len(sizes) > 1 and gi < 3 else 14
        for sz in sizes:
            colx.append(x)
            x += 68 if g == 'People' else (64 if sz == '30B-A3B' else 56)
    ytop, ybot = 186, 214 + 7 * 46 + 26
    last_row = 214 + 7 * 46
    for i, (g, s) in enumerate(cols):
        if f'{g}|{s}' not in ever:
            # header chip marks a column that never sets fitness (an H3 target)
            cw2 = 62 if s in ('30B-A3B', 'clinicians') else 46
            f.rect(colx[i] - cw2 / 2, 149, cw2, 28, fill='#e3e8ee', stroke='none', rx=6, sw=0)
    k = 0
    for g, sizes in groups:
        a, b = colx[k], colx[k + len(sizes) - 1]
        f.text((a + b) / 2, 132, g, 14.5, INK, 700, 'middle')
        f.line(a - 26, 142, b + 26, 142, RULE, 1.4)
        for s in sizes:
            f.text(colx[k], 168, s.strip(), 13, INK2, 400, 'middle')
            k += 1

    def square(cx, cy, r=10):
        f.rect(cx - r, cy - r, 2 * r, 2 * r, fill=SL, stroke=SL, rx=2, sw=1.2)

    def diamond(cx, cy, r=12):
        f.path(f'M{cx:.1f},{cy - r:.1f} L{cx + r:.1f},{cy:.1f} L{cx:.1f},{cy + r:.1f} L{cx - r:.1f},{cy:.1f} Z',
               stroke=SLD, sw=2.2, fill=WHITE)

    for r, (lab, fit) in enumerate(rows):
        yy = 214 + r * 46
        if r == 4:
            f.line(60, yy - 23, colx[-1] + 30, yy - 23, RULE, 1.2, dash='4 5')
        f.text(424, yy + 5, lab, 14, INK, 600, 'end')
        fams = {c.split('|')[0] for c in fit}
        for i, (g, s) in enumerate(cols):
            key = f'{g}|{s}'
            if key in fit:
                f.circle(colx[i], yy, 11, fill=BL, stroke=BL)
            elif lab.endswith('term') and s == 'crowd':
                diamond(colx[i], yy)
            elif g in fams:
                square(colx[i], yy)
            else:
                f.circle(colx[i], yy, 8, fill=AQF, stroke=AQ, sw=1.8)
    f.text(60, 219, 'single reader', 13, MUTED, 600)
    f.text(60, 219 + 4 * 46, 'two readers', 13, MUTED, 600)
    ci = [i for i, (g, s) in enumerate(cols) if s == 'crowd'][0]
    f.text(colx[ci], last_row + 34, 'via predictor', 13, SLD, 600, 'middle')
    ly = 640
    lx = [60, 240, 450, 690, 1040]
    f.circle(lx[0], ly, 10, fill=BL, stroke=BL)
    f.text(lx[0] + 20, ly + 5, 'sets fitness', 14.5, INK)
    square(lx[1], ly, 9)
    f.text(lx[1] + 20, ly + 5, 'same-family holdout', 14.5, INK)
    f.circle(lx[2], ly, 8, fill=AQF, stroke=AQ, sw=1.8)
    f.text(lx[2] + 20, ly + 5, 'other family or people', 14.5, INK)
    f.rect(lx[3] - 16, ly - 12, 32, 24, fill='#e3e8ee', stroke='none', rx=5, sw=0)
    f.text(lx[3] + 24, ly + 5, 'never sets fitness (H3 target)', 14.5, INK)
    diamond(lx[4], ly, 11)
    f.text(lx[4] + 20, ly + 5, 'crowd profile used by predictor', 14.5, INK)
    f.save(os.path.join(OUT, 'reader-design-matrix.svg'))


# ---------------------------------------------------------------------------
# Figure 7 (file order): perceptual profiles predict transfer (illustrative)
# ---------------------------------------------------------------------------
def _spearman(x, y):
    def ranks(v):
        order = sorted(range(len(v)), key=lambda i: v[i])
        r = [0.0] * len(v)
        for k, i in enumerate(order):
            r[i] = float(k)
        return r
    rx, ry = ranks(x), ranks(y)
    n = len(x)
    mx, my = sum(rx) / n, sum(ry) / n
    num = sum((a - mx) * (b - my) for a, b in zip(rx, ry))
    den = math.sqrt(sum((a - mx) ** 2 for a in rx) * sum((b - my) ** 2 for b in ry))
    return num / den


def transfer_cells(seed=9):
    """Illustrative checkpoint-centered gains for 3 checkpoints x 12 held-out VLMs.
    Returns (family, observed, profile forecast, family-and-size forecast) per cell."""
    rnd = random.Random(seed)
    # (family, family-and-size level): Qwen3-VL shares reader A's family; others differ by family and size
    readers = [('Qwen', 0.020), ('Qwen', 0.026), ('Qwen', 0.032), ('Qwen', 0.036),
               ('Gemma', -0.022), ('Gemma', -0.012), ('Gemma', -0.004), ('InternVL', -0.018), ('InternVL', -0.008),
               ('Open4', -0.026), ('Open5', -0.016), ('Closed', 0.002)]
    effect = [lvl + rnd.gauss(0, 0.014) for _, lvl in readers]
    cells = []
    for _ in range(3):
        raw = [e + rnd.gauss(0, 0.030) for e in effect]
        mo = sum(raw) / len(raw)
        mf = sum(l for _, l in readers) / len(readers)
        for (fam, lvl), v in zip(readers, raw):
            o = v - mo
            cells.append((fam, o, 0.75 * o + rnd.gauss(0, 0.032), lvl - mf))
    pm = sum(c[2] for c in cells) / len(cells)
    return [(fam, o, p - pm, q) for fam, o, p, q in cells]


def _within_family(cells, idx):
    """Spearman correlation after removing each family's mean from forecast and observed gain."""
    fams = {c[0] for c in cells}
    mo = {f: sum(c[1] for c in cells if c[0] == f) / sum(1 for c in cells if c[0] == f) for f in fams}
    mp = {f: sum(c[idx] for c in cells if c[0] == f) / sum(1 for c in cells if c[0] == f) for f in fams}
    return _spearman([c[idx] - mp[c[0]] for c in cells], [c[1] - mo[c[0]] for c in cells])


def fig_profile_transfer():
    f = Fig(1300, 656, 'Profiles rank who else gains (illustrative)',
            'Two illustrative scatters of checkpoint-centered observed gain against forecast gain for held-out '
            'VLMs: the registered profile rule ranks readers across and within families, while the '
            'family-and-size predictor assigns one value per family and size.')
    title(f, 'Do battery profiles rank who else gains from a checkpoint?',
          'Illustrative, not data; each point is one checkpoint read by one held-out VLM')
    cells = transfer_cells()
    stats = {}
    for idx in (2, 3):
        stats[idx] = (_spearman([c[idx] for c in cells], [c[1] for c in cells]), _within_family(cells, idx))
    Y0, Y1 = 202, 516
    v0, v1 = -0.12, 0.12
    panels = [(150, 590, 'Registered profile rule', 2), (760, 1200, 'Family and size', 3)]
    jit = random.Random(5)
    for X0, X1, ptitle, idx in panels:
        def mx(v):
            return X0 + (v - v0) / (v1 - v0) * (X1 - X0)

        def my(v):
            return Y1 - (v - v0) / (v1 - v0) * (Y1 - Y0)

        pooled, within = stats[idx]
        f.text(X0, Y0 - 62, ptitle, 15.5, INK, 700)
        col = BLD if idx == 2 else SLD
        f.text(X0, Y0 - 36, 'within-family Spearman ' + f'{within:.2f}'.replace('-', '\u2212'), 15, col, 700)
        f.text(X0, Y0 - 14, 'pooled ' + f'{pooled:.2f}'.replace('-', '\u2212'), 13.5, MUTED, 400)
        if idx == 3:
            f.text(X1 - 8, Y1 - 12, 'x jittered for visibility', 13, MUTED, 400, 'end')
        for v in [-0.1, 0.0, 0.1]:
            lab = f'{v:+.1f}'.replace('+0.0', '0').replace('-', '\u2212')
            f.line(X0, my(v), X1, my(v), '#d9dce1' if v == 0 else '#eceef1', 1.4 if v == 0 else 1)
            f.text(X0 - 12, my(v) + 5, lab, 13.5, INK2, 400, 'end')
            f.line(mx(v), Y1, mx(v), Y1 + 6, INK2, 1.2)
            f.text(mx(v), Y1 + 28, lab, 13.5, INK2, 400, 'middle')
        f.line(mx(0), Y0, mx(0), Y1, '#d9dce1', 1.4)
        f.line(X0, Y0, X0, Y1, INK2, 1.4)
        f.line(X0, Y1, X1, Y1, INK2, 1.4)
        f.text(X0 + 12, Y0 + 18, 'observed gain, centered', 13.5, MUTED)
        f.text((X0 + X1) / 2, Y1 + 62, 'forecast gain, centered (normalized error)', 14, INK, 600, 'middle')
        for fam, o, pr, fs in cells:
            xv = pr if idx == 2 else fs + jit.uniform(-0.0045, 0.0045)
            xv = max(v0 + 0.004, min(v1 - 0.004, xv))
            yv = max(v0 + 0.004, min(v1 - 0.004, o))
            if fam == 'Qwen':
                f.circle(mx(xv), my(yv), 5.2, fill=SL, stroke=WHITE, sw=1.4)
            else:
                f.circle(mx(xv), my(yv), 5.2, fill=AQF, stroke=AQ, sw=1.8)
    ly = 622
    f.circle(160, ly, 7, fill=SL, stroke=WHITE, sw=1.6)
    f.text(176, ly + 5, 'Qwen3-VL (same family as reader A)', 14.5, INK)
    f.circle(560, ly, 7, fill=AQF, stroke=AQ, sw=2)
    f.text(576, ly + 5, 'other-family VLM', 14.5, INK)
    f.save(os.path.join(OUT, 'profile-predicts-transfer.svg'))


# ---------------------------------------------------------------------------
# Figure 6 (file order): transfer-decomposition curve along the search (illustrative)
# ---------------------------------------------------------------------------
def fig_transfer_curve():
    f = Fig(1300, 600, 'Transfer along the search (illustrative)',
            'Illustrative gain over the clinical stabilogram against generation for reader A, never-fitness '
            'VLMs and people, under single-reader fitness and under fitness shared with Gemma 3 12B. The shaded '
            'band is the part of reader A gain those VLMs do not share.')
    title(f, 'Hypothesized: cross-family fitness keeps more of the gain for other VLMs',
          "Illustrative, not data; each bracket is the share of reader A's gain that never-fitness VLMs lack")
    panels = [(110, 540, 'Reader A alone', 'single'), (720, 1130, 'Reader A + Gemma 3 12B', 'ens')]
    Y0, Y1 = 160, 470
    top = 0.5

    def curves(kind, g):
        if kind == 'single':
            a = 0.92 * (1 - math.exp(-g / 10))
            b = 0.50 * (1 - math.exp(-g / 6)) - 0.003 * max(0, g - 10)
            c = 0.44 * (1 - math.exp(-g / 5)) - 0.0075 * max(0, g - 8)
        else:
            a = 0.80 * (1 - math.exp(-g / 11))
            b = 0.71 * (1 - math.exp(-g / 11))
            c = 0.60 * (1 - math.exp(-g / 10))
        return a / 2, b / 2, c / 2

    for X0, X1, ptitle, kind in panels:
        def mx(g):
            return X0 + g / 40 * (X1 - X0)

        def my(v):
            return Y1 - v / top * (Y1 - Y0)

        f.text(X0, Y0 - 26, ptitle, 15.5, INK, 700)
        f.text(X0 + 12, my(0.475), 'gain over stabilogram (normalized error)', 13.5, MUTED)
        for v in [0, 0.25, 0.5]:
            f.line(X0, my(v), X1, my(v), '#eceef1', 1)
            f.text(X0 - 12, my(v) + 5, f'{v:g}', 13.5, INK2, 400, 'end')
        for g in [0, 10, 20, 30, 40]:
            f.line(mx(g), Y1, mx(g), Y1 + 6, INK2, 1.2)
            f.text(mx(g), Y1 + 28, str(g), 13.5, INK2, 400, 'middle')
        f.line(X0, Y0, X0, Y1, INK2, 1.4)
        f.line(X0, Y1, X1, Y1, INK2, 1.4)
        f.text((X0 + X1) / 2, Y1 + 58, 'generation', 14, INK, 600, 'middle')
        gs = [i * 0.5 for i in range(81)]
        A = [(mx(g), my(curves(kind, g)[0])) for g in gs]
        B = [(mx(g), my(curves(kind, g)[1])) for g in gs]
        P = [(mx(g), my(curves(kind, g)[2])) for g in gs]
        band = polyline(A) + ' L' + ' L'.join(f'{x:.1f},{y:.1f}' for x, y in reversed(B)) + ' Z'
        f.add(f'<path d="{band}" fill="{RDF}" stroke="none"/>')
        f.path(polyline(A), stroke=BL, sw=2.8)
        f.path(polyline(B), stroke=AQ, sw=2.8)
        f.path(polyline(P), stroke=SLD, sw=2.6, dash='8 6')
        # bracket at generation 40 spanning reader A and the never-fitness VLMs
        a40, b40, _ = curves(kind, 40)
        bx = X1 + 12
        f.path(f'M{bx - 5:.1f},{my(a40):.1f} H{bx:.1f} V{my(b40):.1f} H{bx - 5:.1f}', stroke=RDD, sw=2)
        f.text(bx + 8, (my(a40) + my(b40)) / 2 + 5, f'{100 * (1 - b40 / a40):.0f}% unshared', 14, RDD, 700)
    ly = 566
    items = [(BL, None, 'reader A (Qwen3-VL-8B)', 110), (AQ, None, 'never-fitness VLMs', 420),
             (SLD, '8 6', 'people', 680)]
    for col, dash, lab, lx in items:
        f.line(lx, ly, lx + 44, ly, col, 2.8, dash=dash)
        f.text(lx + 56, ly + 5, lab, 14.5, INK)
    f.rect(860, ly - 9, 44, 18, fill=RDF, stroke=RDF, rx=3)
    f.text(916, ly + 5, 'gain those VLMs do not share', 14.5, INK)
    f.save(os.path.join(OUT, 'transfer-decomposition-curve.svg'))


# ---------------------------------------------------------------------------
# Figure 8: co-adaptation drift (illustrative)
# ---------------------------------------------------------------------------
def fig_coadapt():
    f = Fig(1300, 620, 'Co-adaptation drift (illustrative)',
            'Illustrative skill over co-adaptation rounds in two matched panels: with standard fitness the '
            'co-adapted pair improves while fresh readers of the same renders fall; with a frozen-reader term in '
            'the fitness both rise and the gap at round 4 is small.')
    title(f, 'Does co-adaptation leave fresh readers behind?',
          'Illustrative prediction for H5, not data')
    Y0, Y1 = 170, 480
    data = [
        (120, 540, 'Standard fitness', [0.05, 0.15, 0.22, 0.27, 0.30], [0.02, 0.00, -0.05, -0.10, -0.14]),
        (740, 1160, 'Fitness plus frozen-reader term', [0.05, 0.12, 0.17, 0.20, 0.22],
         [0.02, 0.06, 0.08, 0.09, 0.10]),
    ]

    def my(v):
        return Y1 - (v + 0.2) / 0.6 * (Y1 - Y0)

    for X0, X1, ptitle, pair, fresh in data:
        def mx(r):
            return X0 + r / 4 * (X1 - X0)

        f.text(X0, Y0 - 26, ptitle, 15.5, INK, 700)
        f.text(X0 + 12, Y0 + 18, 'skill = 1 \u2212 normalized error, sealed participants', 13.5, MUTED)
        if X0 > 400:
            f.text(X0 + 12, my(0) + 22, '0 = predicting the dev-train mean', 13.5, MUTED)
        for v in [-0.2, 0.0, 0.2, 0.4]:
            f.line(X0, my(v), X1, my(v), '#d9dce1' if v == 0 else '#eceef1', 1.3 if v == 0 else 1)
            f.text(X0 - 12, my(v) + 5, f'{v:.1f}'.replace('-', '\u2212'), 13.5, INK2, 400, 'end')
        for r in range(5):
            f.line(mx(r), Y1, mx(r), Y1 + 6, INK2, 1.2)
            f.text(mx(r), Y1 + 28, str(r), 13.5, INK2, 400, 'middle')
        f.line(X0, Y0, X0, Y1, INK2, 1.4)
        f.line(X0, Y1, X1, Y1, INK2, 1.4)
        f.text((X0 + X1) / 2, Y1 + 58, 'co-adaptation round', 14, INK, 600, 'middle')
        rs = range(5)
        band = polyline([(mx(r), my(v)) for r, v in zip(rs, pair)]) + ' L' + ' L'.join(
            f'{mx(r):.1f},{my(v):.1f}' for r, v in reversed(list(zip(rs, fresh)))) + ' Z'
        f.add(f'<path d="{band}" fill="{RDF}" stroke="none"/>')
        for vals, col in [(pair, BL), (fresh, AQ)]:
            f.path(polyline([(mx(r), my(v)) for r, v in zip(rs, vals)]), stroke=col, sw=2.8)
            for r, v in zip(rs, vals):
                if col == BL:
                    f.circle(mx(r), my(v), 4.5, fill=col, stroke=col, sw=2)
                else:
                    f.rect(mx(r) - 5, my(v) - 5, 10, 10, fill=col, stroke=col, rx=1, sw=1.5)
        bx = X1 + 12
        mid = (my(pair[-1]) + my(fresh[-1])) / 2
        f.path(f'M{bx - 5:.1f},{my(pair[-1]):.1f} H{bx:.1f} V{my(fresh[-1]):.1f} H{bx - 5:.1f}', stroke=RDD, sw=2)
        f.text(bx + 8, mid + 5, f'gap {pair[-1] - fresh[-1]:.2f}', 14, RDD, 700)
    ly = 590
    for col, lab, lx, sq in [(BL, 'co-adapted pair', 120, False), (AQ, 'fresh readers, same renders', 400, True)]:
        f.line(lx, ly, lx + 44, ly, col, 2.8)
        if sq:
            f.rect(lx + 17, ly - 5, 10, 10, fill=col, stroke=col, rx=1, sw=1.5)
        else:
            f.circle(lx + 22, ly, 4.5, fill=col, stroke=col, sw=2)
        f.text(lx + 56, ly + 5, lab, 14.5, INK)
    f.rect(760, ly - 9, 44, 18, fill=RDF, stroke=RDF, rx=3)
    f.text(816, ly + 5, 'skill gap', 14.5, INK)
    f.save(os.path.join(OUT, 'co-adaptation-drift.svg'))


if __name__ == '__main__':
    fig_encodings()
    fig_decomposition()
    fig_oracle()
    fig_loop()
    fig_readers()
    fig_profile_transfer()
    fig_transfer_curve()
    fig_coadapt()
    print('wrote', OUT)
