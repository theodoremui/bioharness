"""Figures for proposal 05: what makes an agent harness easier to improve?

Colour roles used in every figure:
  orange = the monolithic or degraded harness, blue = the structured harness or structural information,
  aqua = verified or improving, slate = neutral process, data and sealed material.
Run: python3 -B output/idea-summaries-build/figs_05.py
"""
import math
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from svglib import Fig, C, INK, INK2, MUTED, RULE, WHITE  # noqa: E402

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
OUT = os.path.join(ROOT, 'docs', 'research-plans', 'images', '05')
os.makedirs(OUT, exist_ok=True)

BLUE, ORANGE, AQUA, SLATE = C['blue'], C['orange'], C['aqua'], C['slate']


def poly(pts):
    return 'M' + ' L'.join(f'{x:.1f},{y:.1f}' for x, y in pts)


def heading(f, t, x=40, y=50):
    f.text(x, y, t, 17, INK, 700)


# ---------------------------------------------------------------- figure 1
def same_outputs():
    f = Fig(1240, 500, 'Same outputs, different futures',
            'Two harnesses, A and S, produce identical scores on every input. A is a single long function, S is '
            'split into typed, logged stages. Under the same optimizer and budget, their illustrative improvement '
            'curves start from the same point and diverge; the hypothesized gap comes from how the code is written.')
    heading(f, 'Same outputs today, different futures under self-improvement')
    f.card(40, 110, 360, 112, 'orange', title='Harness A: one function',
           body='400 lines, constants inlined, nothing logged', tsize=16, bsize=14)
    f.card(40, 296, 360, 112, 'blue', title='Harness S: typed stages',
           body='Logged stages, named config with units, warning-only checks', tsize=16, bsize=14)
    f.card(448, 206, 196, 112, 'white', title='Same outputs', body='Identical scores on every input',
           tsize=16, bsize=14)
    f.arrow([(404, 166), (442, 236)], color=SLATE[0], sw=2)
    f.arrow([(404, 352), (442, 290)], color=SLATE[0], sw=2)

    # schematic plot
    x0, y0, x1, ytop = 770, 420, 1050, 128
    f.text(770, 96, 'Same optimizer, same budget (illustrative)', 15, INK, 700)
    f.line(x0, y0, x1 + 20, y0, INK2, 1.6)
    f.line(x0, y0, x0, ytop, INK2, 1.6)
    f.text(x0 + 10, ytop + 14, 'sealed-test improvement', 13, MUTED)
    f.text(x1 + 20, y0 + 30, 'labelled candidate evaluations', 13, MUTED, anchor='end')
    f.text(x0 + 8, y0 + 30, 'same starting score', 13, INK2, 600, anchor='end')

    def val(k, height, t):
        return y0 - height * (1 - math.exp(-k * t)) / (1 - math.exp(-k))

    def curve(k, height):
        return [(x0 + i / 60 * (x1 - x0), val(k, height, i / 60)) for i in range(61)]
    pb, pa = curve(3.2, 250), curve(2.0, 100)
    f.path(poly(pb), stroke=BLUE[0], sw=3.2)
    f.path(poly(pa), stroke=ORANGE[0], sw=3.2)
    f.circle(x0, y0, 5, fill=INK, stroke=INK)
    f.text(x1 + 12, pb[-1][1] + 5, 'S, typed stages', 14, BLUE[2], 700)
    f.text(x1 + 12, pa[-1][1] + 5, 'A, one function', 14, ORANGE[2], 700)
    tb = 0.95
    bx = x0 + tb * (x1 - x0)
    yb, ya = val(3.2, 250, tb), val(2.0, 100, tb)
    f.line(bx, yb, bx, ya, INK2, 1.6)
    f.line(bx - 6, yb, bx + 6, yb, INK2, 1.6)
    f.line(bx - 6, ya, bx + 6, ya, INK2, 1.6)
    f.text(bx - 12, (yb + ya) / 2 + 5, 'hypothesized gap', 13, INK2, anchor='end')
    f.save(os.path.join(OUT, 'same-outputs-different-futures.svg'))


# ---------------------------------------------------------------- figure 2
def pipeline_two_forms():
    f = Fig(1300, 560, 'The Y-Balance score computed two ways',
            'Top: the StaBLE Y-Balance score computation as one function with inline thresholds; the optimizer gets '
            'only the score error. Bottom: harness S, the same computation from the same cached pose input as five typed stages that '
            'read thresholds from a named config, run two warning-only checks and write a per-stage trace that the '
            'optimizer reads. Task scores are identical.')
    heading(f, 'The StaBLE Y-Balance score, computed two ways')
    # harness A
    f.rect(40, 82, 900, 140, fill=ORANGE[1], stroke=ORANGE[0], rx=12)
    f.text(56, 114, 'Harness A: one function, same cached pose input', 16, INK, 700)
    f.text(56, 150, 'def score_trial(pose):   # 400 lines, literals inline', 13, INK2, mono=True)
    f.text(56, 178, ' ' * 4 + 'for th in (0.7, 0.6, 0.5, 0.4, 0.3): ...', 13, INK2, mono=True)
    f.text(56, 206, ' ' * 4 + 'return score', 13, INK2, mono=True)
    f.card(988, 106, 272, 92, 'white', title='Same task score', body='Optimizer receives: score error only',
           tsize=15, bsize=14)
    f.arrow([(944, 152), (982, 152)], color=SLATE[0], sw=2)

    # harness B
    f.text(40, 262, 'Harness S: typed stages, same cached pose input', 16, INK, 700)
    xs, w, y, h = [40, 292, 544, 796, 1048], 212, 308, 92
    stages = [('Cached pose input', 'RTMPose 2D or OpenCap Monocular 3D'), ('Gap fill, filter', 'cutoff_hz from config'),
              ('Center of mass', 'com_ap_m, com_ml_m'), ('Reach window', 'threshold_mps from config'),
              ('Same task score', 'bounds from dev people')]
    for x, (t, b) in zip(xs, stages):
        f.card(x, y, w, h, 'blue', title=t, body=b, tsize=15, bsize=13)
    for a, b in zip(xs, xs[1:]):
        f.arrow([(a + w + 4, y + h / 2), (b - 6, y + h / 2)], color=SLATE[0], sw=2)
    for k, label in [(1, 'warn only: NaN, shape'), (3, 'warn only: empty window')]:
        cx = xs[k] + w / 2
        f.pill(cx, 271, label, 'aqua', size=13, anchor='middle')
        f.line(cx, 297, cx, y - 1, AQUA[0], 1.6)
    # trace strip
    ty = 456
    for x in xs:
        f.arrow([(x + w / 2, y + h + 4), (x + w / 2, ty - 6)], color=SLATE[0], sw=1.6, dash='5 5')
    f.rect(40, ty, 1220, 66, fill=SLATE[1], stroke=SLATE[0], rx=10)
    f.text(60, ty + 28, 'Optimizer receives: score error plus a per-stage trace', 14, INK, 700)
    f.text(60, ty + 52, 'keypoint confidence, center-of-mass range, window found or empty, feature values', 13, INK2)
    f.save(os.path.join(OUT, 'pipeline-two-forms.svg'))


# ---------------------------------------------------------------- figure 3
def bpt_gate():
    f = Fig(1360, 560, 'Behavior-preserving transformations pass an equivalence gate',
            'A base harness is rewritten with one level of each of five structural factors, matched to a common '
            'token count, and admitted to the study only if differential testing finds identical task scores and '
            'identical tool calls on cached development and selection inputs and on fuzzed inputs.')
    heading(f, 'Rewrite the structure, then test that the behavior did not change')
    cy = 304
    f.card(40, cy - 52, 180, 104, 'white', title='Base harness', body='As written', tsize=16, bsize=14)
    f.rect(262, 84, 362, 440, fill='#fbfcfd', stroke=SLATE[0], rx=14, dash='7 6')
    f.text(280, 116, 'Rewrite using one level per factor', 14, INK2, 700)
    rows = [('M', 'Modularity', 'one function or typed stages'), ('O', 'Observability', 'outputs only or logged stages'),
            ('P', 'Parameters', 'inline or named config'), ('T', 'Checks', 'none or warning-only'),
            ('N', 'Naming', 'opaque, generic or physical')]
    for i, (k, t, b) in enumerate(rows):
        yy = 134 + i * 76
        f.rect(280, yy, 326, 62, fill=BLUE[1], stroke=BLUE[0], rx=10)
        f.text(304, yy + 39, k, 18, BLUE[2], 700, anchor='middle')
        f.text(330, yy + 27, t, 15, INK, 700)
        f.text(330, yy + 50, b, 13, INK2)
    f.arrow([(224, cy), (259, cy)], color=SLATE[0], sw=2)
    f.card(668, cy - 52, 190, 104, 'slate', title='Pad to length', body='Same token count for every variant',
           tsize=16, bsize=14)
    f.arrow([(627, cy), (663, cy)], color=SLATE[0], sw=2)
    f.card(902, cy - 82, 214, 164, 'aqua', title='Equivalence gate',
           body='Scores and tool calls match the base on cached and fuzzed inputs', tsize=16, bsize=14)
    f.arrow([(862, cy), (897, cy)], color=SLATE[0], sw=2)
    f.card(1164, 154, 160, 96, 'aqua', title='Pass', body='Enters study', tsize=16, bsize=14)
    f.card(1164, 358, 160, 96, 'white', title='Fail', body='Discarded', tsize=16, bsize=14)
    f.arrow([(1120, cy - 34), (1159, 210)], color=AQUA[0], sw=2)
    f.arrow([(1120, cy + 34), (1159, 398)], color=SLATE[0], sw=2)
    f.save(os.path.join(OUT, 'bpt-equivalence-gate.svg'))


# ---------------------------------------------------------------- figure 4
def edit_profile():
    f = Fig(1360, 470, 'The single-edit success profile',
            'A proposer LLM makes 30 independent one-step edits to the same parent variant, in three sessions of ten. '
            'Each edit is invalid, valid but not a success, or a success: valid, lowering selection error by at least '
            '1 percent and passing the shrinkage guard. The rates and the mean gain form the profile. Outcomes shown are illustrative.')
    heading(f, 'Many one-step edits from one parent give the profile')
    f.card(40, 160, 180, 92, 'blue', title='One parent', body='Base b, cell c', tsize=16, bsize=14)
    f.card(260, 150, 210, 112, 'white', title='Proposer LLM', body='3 sessions of 10 edits', tsize=16, bsize=14)
    f.arrow([(224, 206), (255, 206)], color=SLATE[0], sw=2)
    gx, gy, s, g, pitch = 610, 139, 30, 9, 52
    centers = [gy + r * pitch + s / 2 for r in range(3)]
    # left bracket fanning the proposer's output to the three sessions
    lb = 512
    f.arrow([(474, 206), (lb - 4, 206)], color=SLATE[0], sw=2)
    f.line(lb, gy, lb, gy + 2 * pitch + s, SLATE[0], 2)
    f.line(lb, gy, lb + 8, gy, SLATE[0], 2)
    f.line(lb, gy + 2 * pitch + s, lb + 8, gy + 2 * pitch + s, SLATE[0], 2)
    for cyy, r in zip(centers, range(3)):
        f.text(gx - 12, cyy + 5, f'session {r + 1}', 13, MUTED, anchor='end')
    f.text(gx, gy - 18, '30 edits, each of the same parent (illustrative)', 14, INK, 700)
    pattern = ['ivvsviivvv', 'vvivsvvivv', 'ivvvvsvvsv']
    for r, row in enumerate(pattern):
        for c, k in enumerate(row):
            x = gx + c * (s + g)
            yy = gy + r * pitch
            if k == 'i':
                f.rect(x, yy, s, s, fill=SLATE[2], stroke=SLATE[2], rx=5)
            elif k == 'v':
                f.rect(x, yy, s, s, fill=WHITE, stroke=SLATE[0], rx=5)
            else:
                f.rect(x, yy, s, s, fill=AQUA[0], stroke=AQUA[0], rx=5)
    gx1 = gx + 10 * (s + g) - g
    # right bracket spanning all three sessions
    rb = gx1 + 12
    f.line(rb, gy, rb, gy + 2 * pitch + s, SLATE[0], 2)
    f.line(rb - 6, gy, rb, gy, SLATE[0], 2)
    f.line(rb - 6, gy + 2 * pitch + s, rb, gy + 2 * pitch + s, SLATE[0], 2)
    f.arrow([(rb + 4, 206), (1036, 206)], color=SLATE[0], sw=2)
    ly = 314
    for i, (fill, stroke, lab) in enumerate([(SLATE[2], SLATE[2], 'invalid'),
                                             (WHITE, SLATE[0], 'valid, not a success'),
                                             (AQUA[0], AQUA[0], 'success: gain 1% or more, guard passed')]):
        yy = ly + i * 34
        f.rect(gx, yy, 22, 22, fill=fill, stroke=stroke, rx=4)
        f.text(gx + 34, yy + 17, lab, 13, INK2)
    f.card(1042, 140, 278, 132, 'aqua', title='Profile',
           body=['v = 24/30 valid', 's = 4/30 successes', 'g, r: from per-edit errors'],
           tsize=16, bsize=14)
    f.save(os.path.join(OUT, 'single-edit-profile.svg'))


# ---------------------------------------------------------------- figure 5
def splits():
    f = Fig(1100, 500, 'Split by participant before anything is built',
            'The 171 StaBLE participants with usable single-camera video are divided once, by person, into 85 '
            'development people, 43 selection people and the 43 sealed test people of the lab pilot. '
            'Normalization bounds come from development people only, and sealed people are scored once per loop.')
    heading(f, 'Split by person first; the sealed people are scored once per loop')
    f.card(40, 196, 270, 112, 'white', title='171 participants',
           body='2,968 single-camera task examples (lab pilot)', tsize=16, bsize=14)
    cards = [(96, 'white', 'Development: 85 people',
              ['Scores and traces the proposer reads', 'Normalization bounds fitted here only']),
             (226, 'white', 'Selection: 43 people',
              ['Defines single-edit success', "Picks each loop's final candidate"]),
             (356, 'slate', 'Sealed test: 43 people',
              ['Never read by proposer or search', 'Final candidate scored once per loop'])]
    for yy, role, t, b in cards:
        f.card(470, yy, 560, 112, role, title=t, body=b, tsize=16, bsize=14)
        f.arrow([(314, 252), (410, 252), (410, yy + 56), (464, yy + 56)], color=SLATE[0], sw=2)
    f.lock(1000, 370, s=1.1, color=SLATE[2])
    f.save(os.path.join(OUT, 'participant-splits.svg'))


# ---------------------------------------------------------------- figure 6
def design():
    f = Fig(1360, 750, 'Two tiers: many cheap edits, fewer loops',
            'Top: the eight-cell resolution IV half fraction over modularity, observability, parameters and checks '
            '(I = MOPT), crossed with 20 base harnesses and three proposers; cells 1 and 8 also get naming and '
            'control arms. Bottom: three of the 20 bases give 96 configurations (32 settings each, naming opaque or '
            'physical). Each gets a profile forecast and a clade estimate from 300 evaluations each, and each predictor is '
            'correlated within base with the observed sealed-test gain of its validation loops.')
    heading(f, 'Tier 1 measures profiles cheaply; tier 2 checks them against full loops')
    # tier 1 band
    f.text(40, 100, 'Tier 1: single-edit profiles', 16, INK, 700)
    f.text(40, 128, 'Eight-cell half fraction (I = MOPT) x 20 bases x 3 proposers', 14, INK2)
    rows = ['modularity', 'observability', 'parameters', 'checks']
    cx0, cw, hy = 270, 66, 176
    cells = [(0, 0, 0), (1, 0, 0), (0, 1, 0), (1, 1, 0), (0, 0, 1), (1, 0, 1), (0, 1, 1), (1, 1, 1)]
    for i in (0, 7):  # cells 1 and 8 carry the naming and control arms
        f.rect(cx0 + i * cw - 27, hy - 26, 54, 204, fill='none', stroke=SLATE[0], rx=10, sw=2, dash='6 5')
    for i in range(8):
        f.text(cx0 + i * cw, hy - 2, f'{i + 1}', 13, MUTED, 600, anchor='middle')
    f.text(cx0 - 46, hy - 2, 'cell', 13, MUTED, anchor='end')
    for j, r in enumerate(rows):
        f.text(cx0 - 46, hy + 45 + j * 40, r, 15, INK, 700, anchor='end')
    for i, (m, o, p) in enumerate(cells):
        t = (m + o + p) % 2  # T = M x O x P in +/- coding, so I = MOPT
        xx = cx0 + i * cw
        for j, v in enumerate((m, o, p, t)):
            yy = hy + 40 + j * 40
            if v:
                f.circle(xx, yy, 11, fill=BLUE[0], stroke=BLUE[0])
            else:
                f.circle(xx, yy, 11, fill=WHITE, stroke=ORANGE[0], sw=2)
    lx = 840
    f.circle(lx + 11, 220, 9, fill=BLUE[0], stroke=BLUE[0])
    f.text(lx + 32, 225, 'structured', 14, INK2)
    f.circle(lx + 11, 260, 9, fill=WHITE, stroke=ORANGE[0], sw=2)
    f.text(lx + 32, 265, 'degraded', 14, INK2)
    f.rect(lx, 288, 22, 22, fill='none', stroke=SLATE[0], rx=5, sw=2, dash='4 3')
    f.text(lx + 32, 305, 'cells 1 and 8 also get naming', 14, INK2)
    f.text(lx + 32, 326, 'and control arms', 14, INK2)

    f.line(40, 378, 1320, 378, RULE, 1.5)
    # tier 2 band
    f.text(40, 416, 'Tier 2: loop validation', 16, INK, 700)
    f.card(40, 512, 270, 136, 'white', title='96 configurations',
           body=['3 of the 20 bases', 'x 32 settings (naming', 'opaque or physical)'], tsize=15, bsize=14)
    ys = [444, 544, 644]
    f.card(410, ys[0], 330, 74, 'blue', title='Profile forecast', body='300 edit evaluations', tsize=15, bsize=14)
    f.card(410, ys[1], 330, 74, 'blue', title='Clade estimate (HGM)', body='3 loops x 100 evaluations',
           tsize=15, bsize=14)
    f.card(410, ys[2], 330, 74, 'aqua', title='Observed sealed-test gain', body='10 loops, B = 100 each',
           tsize=15, bsize=14)
    mids = [y + 37 for y in ys]
    f.line(360, mids[0], 360, mids[2], SLATE[0], 2)
    f.line(314, 580, 360, 580, SLATE[0], 2)
    for m in mids:
        f.arrow([(360, m), (404, m)], color=SLATE[0], sw=2)
    f.card(930, 536, 390, 90, 'white', title='Correlate within base',
           body='each predictor with the observed gain', tsize=15, bsize=14)
    f.line(840, mids[0], 840, mids[2], SLATE[0], 2)
    for m in mids:
        f.line(744, m, 840, m, SLATE[0], 2)
    f.arrow([(840, 581), (924, 581)], color=SLATE[0], sw=2)
    f.save(os.path.join(OUT, 'two-tier-design.svg'))


# ---------------------------------------------------------------- figure 7
def parent_selection():
    f = Fig(1320, 640, 'What each parent-selection rule knows about two new nodes',
            'Hypothesis. One parent has two new children, one with degraded code (orange) and one with structured '
            'code (blue), each with one evaluation and the same outcome. Each row pairs a rule with its estimate for '
            'both nodes, a marker with a bar for its spread: DGM gives both the same development score, HGM gives both '
            'the same clade estimate, and HGM with a structural prior separates them using code features alone. '
            'Positions are illustrative.')
    heading(f, 'Hypothesis: code features separate new nodes that score and count alike')
    # shared input: one parent, two new nodes
    f.rect(40, 112, 120, 44, fill=WHITE, stroke=SLATE[0], rx=10)
    f.text(100, 140, 'parent', 14, INK, 600, anchor='middle')
    for yy, role, lab in [(84, 'orange', 'new node, degraded code'), (140, 'blue', 'new node, structured code')]:
        col, bg, dark = C[role]
        f.arrow([(162, 134), (214, yy + 22)], color=SLATE[0], sw=2)
        f.rect(220, yy, 240, 44, fill=bg, stroke=col, rx=10, sw=2, dash='6 4')
        f.text(340, yy + 28, lab, 14, dark, 700, anchor='middle')
    f.text(520, 122, 'One evaluation each, same outcome', 15, INK, 700)
    f.text(520, 148, 'Each rule below estimates both nodes', 14, INK2)
    f.line(40, 210, 1280, 210, RULE, 1.5)

    px0, px1 = 560, 1250
    rows = [(270, 'white', 'DGM: development score', 'Same value for both nodes'),
            (410, 'white', 'HGM: clade estimate', 'Same counts, same estimate'),
            (550, 'blue', 'HGM with structural prior', 'Hypothesized separation by code')]
    for cy, role, ttl, b in rows:
        f.card(40, cy - 42, 420, 84, role, title=ttl, body=b, tsize=16, bsize=14)
        f.arrow([(464, cy), (530, cy)], color=SLATE[0], sw=2)

    def X(u):
        return px0 + u * (px1 - px0)

    def both(x, yb):  # two coincident nodes: orange ring around a blue dot
        f.circle(x, yb, 10, fill=WHITE, stroke=ORANGE[0], sw=3)
        f.circle(x, yb, 5, fill=BLUE[0], stroke=BLUE[0])

    def spread(lo, hi, yb, color):
        f.rect(X(lo), yb - 6, X(hi) - X(lo), 12, fill=color, stroke=color, rx=6, sw=0, opacity=0.3)

    # row 1: development score; both nodes sit at one value
    yb1 = 284
    f.line(px0, yb1, px1, yb1, INK2, 1.4)
    f.text(px0, yb1 + 24, 'worse', 13, MUTED, anchor='middle')
    f.text(px1, yb1 + 24, 'better', 13, MUTED, anchor='middle')
    both(X(0.72), yb1)
    f.text(X(0.72), yb1 - 20, 'both nodes', 13, INK2, anchor='middle')

    def axis(yb):
        f.line(px0, yb, px1, yb, INK2, 1.4)
        f.text(px0, yb + 24, '0', 13, MUTED, anchor='middle')
        f.text(px1, yb + 24, '1', 13, MUTED, anchor='middle')
        f.text((px0 + px1) / 2, yb + 24, 'clade success rate, with spread (illustrative)', 13, MUTED, anchor='middle')
    # row 2: HGM, one wide shared estimate
    yb2 = 424
    axis(yb2)
    spread(0.06, 0.62, yb2, SLATE[0])
    both(X(0.25), yb2)
    f.text(X(0.25), yb2 - 20, 'both nodes', 13, INK2, anchor='middle')
    # row 3: the prior moves the two nodes apart on the same scale
    yb3 = 564
    axis(yb3)
    spread(0.08, 0.30, yb3, ORANGE[0])
    spread(0.38, 0.64, yb3, BLUE[0])
    f.circle(X(0.18), yb3, 9, fill=WHITE, stroke=ORANGE[0], sw=3)
    f.circle(X(0.51), yb3, 8, fill=BLUE[0], stroke=BLUE[0])
    f.text(X(0.18), yb3 - 20, 'degraded', 13, ORANGE[2], 700, anchor='middle')
    f.text(X(0.51), yb3 - 20, 'structured', 13, BLUE[2], 700, anchor='middle')
    f.save(os.path.join(OUT, 'parent-selection-at-birth.svg'))


# ---------------------------------------------------------------- figure 8
def refactor_first():
    f = Fig(1260, 560, 'When refactoring first pays off',
            'Illustrative accept-if-better model. Search alone removes error at per-evaluation rate r0. '
            'Refactoring first spends a fixed cost in evaluation-equivalents with no gain, then removes error at '
            'a higher rate r1 (0.015 against 0.010). The curves cross at the break-even budget B*, about three times the refactor cost.')
    heading(f, 'Refactoring first can pay off past a break-even budget')
    x0, y0, x1, ytop = 130, 450, 1000, 110
    bmax, r0, r1, br = 120, 0.010, 0.015, 20
    f.line(x0, y0, x1 + 10, y0, INK2, 1.6)
    f.line(x0, y0, x0, ytop, INK2, 1.6)
    base = y0  # zero gain lies on the axis; the cost bracket below marks the flat refactor segment

    def X(bv):
        return x0 + (x1 - x0) * bv / bmax

    def Y(v):
        return base - (base - ytop - 10) * v
    f.rect(X(0), ytop, X(br) - X(0), y0 - ytop, fill=BLUE[1], stroke=BLUE[1], rx=0, sw=0, opacity=0.7)
    f.text((X(0) + X(br)) / 2, ytop + 40, 'refactoring,', 13, BLUE[2], anchor='middle')
    f.text((X(0) + X(br)) / 2, ytop + 58, 'no gain yet', 13, BLUE[2], anchor='middle')
    so = [(X(bv), Y(1 - (1 - r0) ** bv)) for bv in range(0, bmax + 1)]
    rf = [(X(bv), Y(0 if bv < br else 1 - (1 - r1) ** (bv - br))) for bv in range(0, bmax + 1)]
    f.path(poly(so), stroke=ORANGE[0], sw=3.2)
    f.path(poly(rf), stroke=BLUE[0], sw=3.2)
    f.text(X(bmax) + 12, rf[-1][1] + 5, 'refactor first', 14, BLUE[2], 700)
    f.text(X(bmax) + 12, so[-1][1] + 5, 'search only', 14, ORANGE[2], 700)
    bstar = br * math.log(1 - r1) / (math.log(1 - r1) - math.log(1 - r0))
    ys = Y(1 - (1 - r0) ** bstar)
    f.line(X(bstar), ys, X(bstar), y0, INK2, 1.4, dash='5 5')
    f.circle(X(bstar), ys, 6, fill=INK, stroke=INK)
    f.text(X(bstar) + 14, ys + 30, 'B* ≈ 3× refactor cost', 15, INK, 700)
    f.text(x0 - 10, y0 + 5, '0', 14, MUTED, anchor='end')
    # refactor cost interval under the axis
    yc = y0 + 12
    f.line(X(0), yc, X(br), yc, BLUE[0], 2)
    f.line(X(0), yc - 5, X(0), yc + 5, BLUE[0], 2)
    f.line(X(br), yc - 5, X(br), yc + 5, BLUE[0], 2)
    f.text((X(0) + X(br)) / 2, y0 + 34, 'refactor cost', 14, BLUE[2], 700, anchor='middle')
    f.text((x0 + x1) / 2, y0 + 70, 'budget in evaluation-equivalents', 14, MUTED, anchor='middle')
    f.text(x0 + 12, ytop - 12, 'expected fraction of error removed (illustrative)', 14, MUTED)
    f.save(os.path.join(OUT, 'refactor-first-break-even.svg'))


if __name__ == '__main__':
    same_outputs()
    pipeline_two_forms()
    bpt_gate()
    edit_profile()
    splits()
    design()
    parent_selection()
    refactor_first()
    print('ok')
