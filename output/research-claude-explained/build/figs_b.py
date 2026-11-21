import math, sys
from svglib import *

OUT = sys.argv[1]
S = C['slate'][0]


# ---------------------------------------------------------------- splits
def fig_split(variant):
    test_n = {'v1': 43, 'v2': 43, 'v3': 43, 'v5': 60, 'v7': 60}[variant]
    dev_n = 171 - test_n
    sealed = variant in ('v3', 'v5', 'v7')
    H = 600 if variant in ('v5', 'v7') else 540
    f = Fig(1300, H, 'How participants are divided',
            f'Of 171 participants with usable video, {test_n} form the {"sealed" if sealed else "test"} set and '
            f'{dev_n} form the development set, which is cut into five folds. Each person stays on one side.')
    f.text(24, 44, '171 participants with usable single-camera video', 16, INK, 700)
    f.text(24, 66, 'one dot = one person', 12.5, MUTED)
    # dot grid 19 x 9
    order = ['t'] * test_n
    if variant == 'v3':
        order += ['f'] * 43 + ['d'] * (dev_n - 43)
    else:
        order += ['d'] * dev_n
    # spread test dots through the grid deterministically
    import random
    rnd = random.Random(7)
    rnd.shuffle(order)
    for i, kind in enumerate(order):
        r, c = divmod(i, 19)
        x, y = 34 + c * 21, 92 + r * 21
        if kind == 't':
            f.circle(x, y, 7, fill=C['red'][0], stroke=WHITE, sw=1.5)
        elif kind == 'f':
            f.circle(x, y, 7, fill=C['blue'][1], stroke=C['blue'][0], sw=2)
        else:
            f.circle(x, y, 7, fill=C['blue'][0], stroke=WHITE, sw=1.5)
    ly = 92 + 9 * 21 + 8
    f.circle(34, ly, 7, fill=C['red'][0], stroke=WHITE, sw=1.5)
    f.text(48, ly + 4, f'{"sealed" if sealed else "test"} ({test_n})', 12.5, INK2)
    f.circle(170, ly, 7, fill=C['blue'][0], stroke=WHITE, sw=1.5)
    if variant == 'v3':
        f.text(184, ly + 4, f'development ({dev_n - 43})', 12.5, INK2)
        f.circle(34, ly + 24, 7, fill=C['blue'][1], stroke=C['blue'][0], sw=2)
        f.text(48, ly + 28, 'former test set, now part of development (43)', 12.5, INK2)
    else:
        f.text(184, ly + 4, f'development ({dev_n})', 12.5, INK2)
    # right side boxes
    X = 470
    if variant in ('v1', 'v2'):
        ttl = f'Test set: {test_n} people'
        body = 'The same 43 people as the lab pilot’s test set, so results stay comparable. Used once, after every choice is fixed.'
    elif variant == 'v3':
        ttl = f'Sealed confirmatory set: {test_n} people'
        body = 'Drawn from people nobody has used to evaluate a method. Stored separately and opened once, after every method is frozen.'
    else:
        ttl = f'Sealed set: {test_n} people, reserved first'
        body = 'Set aside before this study’s development work, from people never in the pilot’s test set (some helped train the pilot’s models). Opened once, at the end.'
    f.rect(X, 84, 806, 92, fill=C['red'][1], stroke=C['red'][0], rx=12)
    f.lock(X + 16, 98, 1.0)
    f.text(X + 40, 112, ttl, 15, INK, 700)
    f.para(X + 16, 138, body, 770, 13, INK2)
    f.rect(X, 196, 806, 150, fill=C['blue'][1], stroke=C['blue'][0], rx=12)
    dtitle = f'Development set: {dev_n} people in five folds'
    f.text(X + 16, 222, dtitle, 15, INK, 700)
    for k in range(5):
        fx = X + 16 + k * 156
        f.rect(fx, 238, 144, 40, fill=WHITE, stroke=C['blue'][0], rx=8)
        f.text(fx + 72, 263, f'Fold {k + 1}', 13.5, INK, 600, 'middle')
    note = 'Train on four folds, check on the fifth, then rotate (cross-validation).'
    if variant != 'v1':
        note += ' Folds are balanced by balance score, age group and elite-athlete status.'
    f.para(X + 16, 302, note, 770, 13, INK2)
    # bottom insets
    by = 370
    f.rect(24, by, 600, 144, fill=PANEL, stroke=RULE, rx=12)
    f.text(42, by + 28, 'Each person’s videos stay together', 14.5, INK, 700)
    f.person(60, by + 46, 54, INK2, 2)
    for k in range(18):
        f.rect(96 + k * 27, by + 58, 21, 21, fill=C['blue'][0], stroke=WHITE, rx=4, sw=1)
    f.para(96, by + 106, 'Up to 18 task videos of one person, always on the same side of every split', 500, 12.5, INK2)
    if variant != 'v1':
        f.rect(650, by, 626, 144, fill=WHITE, stroke=C['orange'][0], rx=12, dash='6 4')
        f.text(668, by + 28, 'Learned from training people only', 14.5, INK, 700)
        items = ('Rescaling endpoints (lowest and highest values), the average used when a method fails, '
                 'examples shown to the model' + (', probe videos, teacher demonstrations' if variant in ('v5', 'v7') else '')
                 + '. StaBLE’s published endpoints used all 180 people, so they are recomputed.')
        f.para(668, by + 54, items, 590, 12.5, INK2)
    else:
        f.rect(650, by, 626, 144, fill=WHITE, stroke=RULE, rx=12)
        f.text(668, by + 28, 'One evaluation of the test set', 14.5, INK, 700)
        f.para(668, by + 54, 'Prompts, harness code and model weights are chosen using development folds only. '
               'The test set is scored once at the end, so no choice can be tuned to it.', 590, 12.5, INK2)
    if variant in ('v5', 'v7'):
        hy = 548
        f.text(24, hy + 4, 'Held-out tasks:', 13.5, INK, 700)
        for k in range(18):
            held = k in (2, 13, 7)
            f.rect(140 + k * 25, hy - 12, 19, 19, fill=C['red'][0] if held else '#cbd5e1', stroke=WHITE, rx=4, sw=1)
        t = ('Semi-Tandem, Gait-Backwards and Functional Reach are never trained on'
             + ('; their scales come from a calibration set.' if variant == 'v7' else '.'))
        f.para(600, hy + 4, t, 680, 12.5, INK2)
    f.save(f'{OUT}/fig_split_{variant}.svg')


# ---------------------------------------------------------------- bootstrap
def fig_bootstrap(seeds=True):
    H = 640 if seeds else 430
    f = Fig(1300, H, 'Measuring uncertainty by resampling',
            'Resampling the tested people with replacement many times gives a range of plausible differences between two '
            'methods; retraining with new random seeds shows how much a single training run varies.')
    f.text(24, 44, 'A   Resample the tested people (the bootstrap)', 16, INK, 700)
    people = ['P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8']

    def chips(x, y, labs, role='slate'):
        for k, lab in enumerate(labs):
            f.rect(x + k * 44, y, 38, 28, fill=C[role][1], stroke=C[role][0], rx=7, sw=1.2)
            f.text(x + k * 44 + 19, y + 19, lab, 12, INK, 600, 'middle')
    f.text(24, 82, 'tested people', 12.5, MUTED)
    chips(130, 64, people)
    f.text(130 + 8 * 44 + 4, 84, '… 43 in all', 12.5, MUTED)
    rows = [(['P3', 'P3', 'P7', 'P1', 'P8', 'P2', 'P2', 'P5'], '+0.06'),
            (['P6', 'P1', 'P4', 'P4', 'P8', 'P2', 'P7', 'P7'], '+0.03'),
            (['P2', 'P5', 'P5', 'P3', 'P8', 'P6', 'P1', 'P4'], '+0.08')]
    for j, (labs, d) in enumerate(rows):
        y = 118 + j * 42
        f.text(24, y + 19, f'resample {j + 1}', 12.5, MUTED)
        chips(130, y, labs, 'blue')
        f.text(130 + 8 * 44 + 10, y + 19, 'difference', 12.5, INK2)
        f.text(130 + 8 * 44 + 140, y + 19, d, 13.5, INK, 700, 'end')
    f.text(130, 118 + 3 * 42 + 14, '… repeated 10,000 times; some people appear twice, some not at all', 12.5, MUTED)
    # histogram
    hx, hy, hw, hh = 720, 70, 520, 200
    lo, hi = -0.03, 0.13
    nb = 32
    mu, sd = 0.05, 0.022
    X = lambda v: hx + (v - lo) / (hi - lo) * hw
    for b in range(nb):
        a = lo + b * (hi - lo) / nb
        c = a + (hi - lo) / nb / 2
        h = math.exp(-0.5 * ((c - mu) / sd) ** 2)
        inside = mu - 1.96 * sd <= c <= mu + 1.96 * sd
        col = C['blue'][0] if inside else '#b8c7da'
        f.rect(X(a) + 1, hy + hh - h * hh, hw / nb - 2, h * hh, fill=col, stroke=col, rx=2, sw=0)
    f.line(hx, hy + hh, hx + hw, hy + hh, MUTED, 1.2)
    for v in [0.0, 0.05, 0.10]:
        f.text(X(v), hy + hh + 18, f'{v:+.2f}' if v else '0', 12, MUTED, anchor='middle')
    f.line(X(0), hy - 4, X(0), hy + hh, C['red'][0], 1.5, '5 4')
    f.text(X(0) - 6, hy + 8, 'no difference', 12, C['red'][2], anchor='end')
    a, b = mu - 1.96 * sd, mu + 1.96 * sd
    f.path(f'M{X(a):.1f},{hy + hh + 34} V{hy + hh + 42} H{X(b):.1f} V{hy + hh + 34}', INK, 1.6)
    f.text((X(a) + X(b)) / 2, hy + hh + 60, f'95% interval: {a:+.3f} to {b:+.3f}', 13, INK, 700, 'middle')
    f.text(hx + hw / 2, hy - 18, 'differences from all 10,000 resamples', 12.5, INK2, anchor='middle')
    f.para(24, 335, 'The middle 95% of these differences is the confidence interval. If it lies entirely above zero, '
           'the gain is unlikely to come from the luck of which people happened to be tested.', 640, 13, INK2)
    if seeds:
        f.line(24, 410, 1276, 410, RULE, 1)
        f.text(24, 448, 'B   Retrain with new random seeds', 16, INK, 700)
        f.para(24, 474, 'Training involves random choices (which examples come first, which attempts are sampled). '
               'A seed fixes those choices. A lucky run moves every participant at once, so resampling people cannot remove it.',
               560, 13, INK2)
        for j, (sd_, d) in enumerate([('seed 1', '+0.07'), ('seed 2', '+0.02'), ('seed 3', '+0.05')]):
            y = 440 + j * 58
            f.rect(650, y, 110, 40, fill=PANEL, stroke=RULE, rx=8)
            f.text(705, y + 25, sd_, 13, INK, 600, 'middle')
            f.arrow([(762, y + 20), (796, y + 20)], S)
            f.rect(800, y, 170, 40, fill=C['blue'][1], stroke=C['blue'][0], rx=8)
            f.text(885, y + 25, 'train, then test', 13, INK, 600, 'middle')
            f.arrow([(972, y + 20), (1006, y + 20)], S)
            f.text(1012, y + 25, f'difference {d}', 13.5, INK, 700)
        f.para(650, 622, 'A claim about a training method uses both kinds of spread.', 600, 13, INK2)
    f.save(f'{OUT}/fig_bootstrap{"" if seeds else "_people"}.svg')


# ---------------------------------------------------------------- stages
STAGES = {
    'v2': [('A', 'Re-baseline', 'Are the old methods mostly shrinking toward the average?', 'If the fine-tuned model keeps differences (slope above 0.8), error stays the main measure'),
           ('B', 'Frozen agent', 'Do tools alone help an untrained agent?', 'If not, read the failure logs before optimizing'),
           ('C', 'Prompts and harness', 'Do better instructions and harness code help at low cost?', 'Carry the better of the two forward'),
           ('D', 'Fine-tuning', 'Does copying successful runs improve tool choice?', 'Carry forward if it beats stage C'),
           ('E', 'Reinforcement learning', 'Does rewarding closeness to the reference help further?', 'The final candidate'),
           ('T', 'Test', 'Do the development findings hold on new people?', 'Everything frozen; 43 test people scored once')],
    'v4': [('0', 'Groundwork', 'Is the protocol sound, and is the study large enough?', 'Power below 80%: enlarge the sealed set to 60'),
           ('1', 'Re-baseline', 'How far do existing methods get, and through what?', 'If age and sex rank people as well, age-adjusted rank agreement joins the primary measure'),
           ('2', 'Frozen agent', 'Do tools alone help?', 'Under 30% verified coverage: fix the harness first'),
           ('3', 'Prompt and harness search', 'What do text-level changes add per GPU-hour?', 'Best harness becomes the training harness'),
           ('4', 'Warm start', 'Does the privileged teacher help?', 'Keep both warm starts for stage 5'),
           ('5', 'Reinforcement learning', 'Do verified per-feature rewards beat score-only rewards?', 'Freeze every method'),
           ('6', 'Confirmation', 'Do the development findings hold?', 'Sealed set opened once')],
    'v5': [('0', 'Groundwork', 'Is the protocol sound, and is the study large enough?', 'Power below 60%: report estimates only'),
           ('1', 'Re-baseline', 'What do existing methods achieve, and from what?', 'If age and sex rank people as well, age-adjusted rank agreement joins the primary measure'),
           ('2', 'Frozen agent', 'Do tools alone help?', 'Under 30% verified coverage: fix the harness first'),
           ('3', 'Prompt and harness search', 'What do text-level changes add per GPU-hour?', 'Best harness becomes the training harness'),
           ('4', 'Warm start', 'Does the privileged teacher help?', 'The better warm start feeds every RL arm'),
           ('5', 'Reinforcement learning', 'Does the verified per-feature reward win, and is verification needed?', 'Freeze all components'),
           ('6', 'World model', 'Can the agent spend less compute?', 'Exploratory'),
           ('7', 'Confirmation', 'Do findings hold for new people and new tasks?', 'Sealed set and held-out tasks opened once')],
}
STAGES['v6'] = [s if s[0] not in ('2', '5', '6') else
                {'2': ('2', 'Frozen agent', 'Do tools alone help?', 'Low checked coverage: fix the harness first'),
                 '5': ('5', 'Reinforcement learning', 'Do checked per-feature rewards win, and is the check needed?', 'Freeze all components'),
                 '6': ('6', 'Tool-outcome model', 'Can the agent spend less compute?', 'Exploratory')}[s[0]]
                for s in STAGES['v5']]
STAGES['v7'] = [s if s[0] not in ('3', '4', '5', '6') else
                {'3': ('3', 'Prompt and harness search', 'What do text-level changes add per GPU-hour?', 'At most 20 validation checks per run; the best harness is used for training'),
                 '4': ('4', 'Warm start', 'Does the privileged teacher help?', 'RL starts from the better warm start, whichever it is'),
                 '5': ('5', 'Reinforcement learning', 'Do checked per-feature rewards win, and is the check needed?', 'Freeze all components'),
                 '6': ('6', 'Cost-aware RL', 'Can the agent spend less compute?', 'Exploratory')}[s[0]]
                for s in STAGES['v6']]


def fig_stages(variant):
    st = STAGES[variant]
    per = 4 if len(st) > 6 else 3
    W = (1252 - (per - 1) * 28) / per
    rows = math.ceil(len(st) / per)
    CH = 232
    f = Fig(1300, 24 + rows * (CH + 34) + 10, 'The research plan as stages with decisions',
            'Each stage asks one question on development data and ends with a decision that shapes the next stage; '
            'the held-back people are used only in the last stage.')
    for i, (sid, title, q, dec) in enumerate(st):
        r, c = divmod(i, per)
        x, y = 24 + c * (W + 28), 24 + r * (CH + 34)
        last = i == len(st) - 1
        role = 'red' if last else 'white'
        f.rect(x, y, W, CH, fill=C[role][1], stroke=C[role][0], rx=12)
        lab = f'Stage {sid}' if sid not in ('T',) else 'Final'
        if last:
            f.lock(x + 14, y + 11, 0.85)
        f.text(x + (34 if last else 14), y + 24, lab.upper(), 11.5, MUTED, 700)
        f.text(x + 14, y + 47, title, 14.5, INK, 700)
        yy = f.para(x + 14, y + 72, q, W - 28, 13, INK)
        f.line(x + 14, y + 118, x + W - 14, y + 118, RULE, 1)
        f.text(x + 14, y + 139, 'Decision', 11.5, MUTED, 600)
        f.para(x + 86, y + 139, dec, W - 100, 12, INK2)
        if not last:
            if c < per - 1:
                f.arrow([(x + W + 3, y + CH / 2), (x + W + 25, y + CH / 2)], S)
            else:
                ny = y + CH + 34
                f.arrow([(x + W / 2, y + CH + 2), (x + W / 2, y + CH + 17), (24 + W / 2, y + CH + 17), (24 + W / 2, ny - 3)], S)
    f.save(f'{OUT}/fig_stages_{variant}.svg')


# ---------------------------------------------------------------- cancel
def fig_cancel():
    ref = [0.55, 0.75, 1.00]
    A = [0.75, 0.55, 1.00]
    B = [0.60, 0.80, 0.95]
    names = ['peak upward speed', 'peak ankle angle', 'hold time']
    f = Fig(1300, 500, 'Opposite feature errors can cancel in the score',
            'Attempt A gets the task score exactly right from two wrong features; attempt B has small errors everywhere. '
            'A reward on the final score prefers A; a per-feature reward prefers B.')
    for k, (title, att) in enumerate([('Attempt A', A), ('Attempt B', B)]):
        x0 = 24 + k * 636
        f.rect(x0, 24, 616, 452, fill=PANEL, stroke=RULE, rx=14)
        f.text(x0 + 20, 56, title, 16, INK, 700)
        L, R = x0 + 190, x0 + 580
        for j, (n, rv, av) in enumerate(zip(names, ref, att)):
            y = 100 + j * 66
            f.text(x0 + 20, y + 5, n, 13.5, INK)
            f.line(L, y, R, y, '#cfd5dc', 6)
            for t in [0, 0.5, 1]:
                f.text(L + t * (R - L), y + 26, f'{t:g}', 11, MUTED, anchor='middle')
            xr, xa = L + rv * (R - L), L + av * (R - L)
            if abs(xa - xr) > 1:
                f.line(xr, y, xa, y, C['red'][0], 6, cap='butt')
            f.add(f'<path d="M{xr:.1f},{y - 11} l7,11 l-7,11 l-7,-11 z" fill="{C["orange"][0]}" stroke="#fff" stroke-width="1.5"/>')
            f.circle(xa, y, 8, fill=C['blue'][0], stroke=WHITE, sw=2)
            f.text(R + 10 if False else x0 + 600, y + 5, f'{abs(av - rv):.2f}', 13, INK, 700, 'end') if False else None
        sc = sum(att) / 3
        se = abs(sc - sum(ref) / 3)
        fe = sum(abs(a - r) for a, r in zip(att, ref)) / 3
        f.line(x0 + 20, 300, x0 + 596, 300, RULE, 1)
        f.text(x0 + 20, 330, f'task score {sc:.3f}   (reference {sum(ref) / 3:.3f})', 13.5, INK2)
        f.text(x0 + 20, 362, 'error of the final score', 13.5, INK)
        f.text(x0 + 300, 362, f'{se:.3f}', 15, INK, 700)
        f.text(x0 + 20, 392, 'average error per feature', 13.5, INK)
        f.text(x0 + 300, 392, f'{fe:.3f}', 15, INK, 700)
        win = 'Final-score reward prefers this one' if k == 0 else 'Per-feature reward prefers this one'
        f.pill(x0 + 20, 420, win, 'yellow' if k == 0 else 'aqua', 12.5)
    f.add(f'<path d="M{60},{486} l6,9 l-6,9 l-6,-9 z" fill="{C["orange"][0]}"/>') if False else None
    f.save(f'{OUT}/fig_cancel.svg')


# ---------------------------------------------------------------- check panels
def chip(f, x, y, t, role='white', w=None, mono=False, size=12.5):
    w = w or tw(t, size) + 22
    f.rect(x, y, w, 30, fill=C[role][1], stroke=C[role][0], rx=8, sw=1.2)
    f.text(x + w / 2, y + 20, t, size, INK, 600, 'middle', mono=mono)
    return w


def mini_curve(f, x, y, w, h, steep=1.0, color=None, dash=None):
    pts = []
    for k in range(41):
        t = k / 40
        v = 1 / (1 + math.exp(-(t - 0.35) * 30 * steep)) - 1 / (1 + math.exp(-(t - 0.85) * 30))
        pts.append((x + t * w, y + h - 4 - v * (h - 10)))
    f.path('M' + ' L'.join(f'{a:.1f},{b:.1f}' for a, b in pts), color or C['blue'][0], 2.2, dash=dash)


def panel_replay(f, x, y, w, noisy=False):
    f.text(x + 16, y + 30, 'Replay' + (' + noisy copy' if noisy else ''), 15.5, INK, 700)
    chip(f, x + 16, y + 50, 'peak_speed(com, marks)', 'blue', mono=True, size=12)
    f.text(x + 16, y + 102, 'run again on the cited tool outputs', 12.5, INK2)
    chip(f, x + 16, y + 112, '0.31', 'white', 64)
    f.text(x + 92, y + 132, '=', 15, INK, 700)
    chip(f, x + 110, y + 112, '0.31', 'white', 64)
    f.check(x + 196, y + 127)
    yy = y + 168
    if noisy:
        f.text(x + 16, yy, 'run on a copy with tiny added noise', 12.5, INK2)
        chip(f, x + 16, yy + 10, '0.31', 'white', 64)
        f.text(x + 92, yy + 30, '≈', 15, INK, 700)
        chip(f, x + 110, yy + 10, '0.31', 'white', 64)
        f.check(x + 196, yy + 25)
        yy += 66
    rule = ('Same inputs must give the same number, and a copy with noise far below measurement precision must give '
            'nearly the same number. This can expose a function that looks up a stored answer for this exact video.'
            if noisy else 'Re-running the submitted code on the evidence it cites must give the submitted number.')
    f.para(x + 16, yy + 4, rule, w - 32, 12.5, INK2)


def panel_dependence(f, x, y, w):
    f.text(x + 16, y + 30, 'Dependence', 15.5, INK, 700)
    f.text(x + 16, y + 62, 'run the code on two other videos of the task', 12.5, INK2)
    chip(f, x + 16, y + 74, 'peak_speed(…)', 'blue', mono=True, size=12)
    chip(f, x + 170, y + 74, '0.27', 'white', 56); chip(f, x + 234, y + 74, '0.36', 'white', 56)
    f.check(x + w - 30, y + 89)
    chip(f, x + 16, y + 118, 'return 0.18', 'red', mono=True, size=12)
    chip(f, x + 170, y + 118, '0.18', 'white', 56); chip(f, x + 234, y + 118, '0.18', 'white', 56)
    f.check(x + w - 30, y + 133, ok=False)
    f.para(x + 16, y + 178, 'The value must change when the input changes. A function that returns a typical number '
           'whatever it is given fails, which blocks typing a guess and attaching an unrelated pointer.', w - 32, 12.5, INK2)


def panel_material(f, x, y, w):
    f.text(x + 16, y + 30, 'Material response', 15.5, INK, 700)
    f.text(x + 16, y + 62, 'two probe videos: a slow riser and a fast riser', 12.5, INK2)
    f.text(x + 16, y + 92, 'agent code', 12, MUTED)
    chip(f, x + 150, y + 74, '0.12', 'white', 56); chip(f, x + 214, y + 74, '0.41', 'white', 56)
    f.check(x + w - 30, y + 89)
    f.text(x + 16, y + 136, 'mean + tiny term', 12, MUTED)
    chip(f, x + 150, y + 118, '0.180', 'red', 62); chip(f, x + 220, y + 118, '0.181', 'red', 62)
    f.check(x + w - 30, y + 133, ok=False)
    f.para(x + 16, y + 178, 'The two results must differ by at least a quarter of the feature’s typical spread in '
           'training data. A constant, or a constant plus a negligible term, fails.', w - 32, 12.5, INK2)


def panel_probes(f, x, y, w):
    f.text(x + 16, y + 30, 'Known answers', 15.5, INK, 700)
    f.text(x + 16, y + 58, 'four development videos with known values (m/s)', 12.5, INK2)
    f.text(x + 16, y + 86, 'known', 12, MUTED)
    f.text(x + 16, y + 122, 'agent code', 12, MUTED)
    f.text(x + 16, y + 158, 'return 0.18', 12, MUTED, mono=True)
    known, got = ['0.12', '0.15', '0.38', '0.42'], ['0.13', '0.15', '0.36', '0.43']
    for k in range(4):
        cx = x + 128 + k * 54
        chip(f, cx, y + 68, known[k], 'orange', 46, size=12)
        chip(f, cx, y + 104, got[k], 'white', 46, size=12)
        chip(f, cx, y + 140, '0.18', 'red', 46, size=12)
    f.text(x + 128 + 50, y + 192, 'slow risers', 11.5, MUTED, anchor='middle')
    f.text(x + 128 + 158, y + 192, 'fast risers', 11.5, MUTED, anchor='middle')
    f.check(x + w - 26, y + 119)
    f.check(x + w - 26, y + 155, ok=False)
    f.para(x + 16, y + 220, 'Run on probe videos whose answers are known, the code must land close to those answers and '
           'put the slow risers below the fast ones.', w - 32, 12.5, INK2)


def panel_required(f, x, y, w):
    f.text(x + 16, y + 30, 'Required signal', 15.5, INK, 700)
    f.text(x + 16, y + 56, 'steepen the center-of-mass rise', 12.5, INK2)
    mini_curve(f, x + 16, y + 64, 120, 60, 1.0, '#9aa3af')
    mini_curve(f, x + 16, y + 64, 120, 60, 2.2, C['blue'][0])
    f.text(x + 150, y + 82, 'StaBLE\u2019s code: speed goes up', 12.5, INK2)
    f.text(x + 150, y + 104, 'agent\u2019s code: speed goes up', 12.5, INK2)
    f.check(x + w - 26, y + 99)
    f.text(x + 16, y + 150, 'code using only the time marks', 12, MUTED)
    f.text(x + 16, y + 170, 'output unchanged', 12, INK2)
    f.check(x + w - 26, y + 160, ok=False)
    f.para(x + 16, y + 214, 'Each feature has a few planned edits of the signal it is defined on. The agent’s code must '
           'react as StaBLE’s released code reacts to the same edit, including edits that should change nothing.',
           w - 32, 12.5, INK2)


def panel_range(f, x, y, w):
    f.text(x + 16, y + 30, 'Range', 15.5, INK, 700)
    L, R = x + 30, x + w - 30
    f.line(L, y + 90, R, y + 90, '#cfd5dc', 6)
    a, b = L + (R - L) * 0.25, L + (R - L) * 0.75
    f.line(a, y + 90, b, y + 90, C['aqua'][0], 6)
    f.text(a, y + 116, '0.03', 11.5, MUTED, anchor='middle')
    f.text(b, y + 116, '0.52 m/s', 11.5, MUTED, anchor='middle')
    f.text((a + b) / 2, y + 70, 'training range', 12, INK2, anchor='middle')
    f.text(L, y + 70, 'widened', 11.5, MUTED)
    f.text(R, y + 70, 'widened', 11.5, MUTED, anchor='end')
    v = a + (b - a) * (0.31 - 0.03) / 0.49
    f.circle(v, y + 90, 8, fill=C['blue'][0], stroke=WHITE, sw=2)
    f.text(v, y + 140, '0.31 ✓', 12.5, INK, 700, 'middle')
    f.para(x + 16, y + 178, 'The value must lie within the training range widened by half its width on each side, and '
           'within physical limits (hold time between 0 and 5 s). A speed of 2.4 m/s for rising onto the toes fails.', w - 32, 12.5, INK2)


def fig_check(variant):
    panels = {'v3': [panel_replay, panel_dependence, panel_range],
              'v4': [panel_replay, panel_material, panel_range],
              'v5': [panel_replay, panel_probes, panel_range],
              'v7': [lambda f, x, y, w: panel_replay(f, x, y, w, True), panel_required, panel_probes, panel_range]}[variant]
    n = len(panels)
    per = 2 if n == 4 else 3
    W = (1252 - (per - 1) * 20) / per
    PH = 300 if n == 4 else 300
    rows = math.ceil(n / per)
    foot = variant in ('v5', 'v7')
    H = 24 + rows * (PH + 20) + (84 if foot else 4)
    f = Fig(1300, H, 'The check on each submitted feature',
            'Tests applied to every submitted feature; none needs the reference value for the video being analysed.')
    for i, p in enumerate(panels):
        r, c = divmod(i, per)
        x, y = 24 + c * (W + 20), 24 + r * (PH + 20)
        f.rect(x, y, W, PH, fill=PANEL, stroke=RULE, rx=14)
        p(f, x, y, W)
    if foot:
        fy = 24 + rows * (PH + 20)
        f.rect(24, fy, 1252, 64, fill=WHITE, stroke=C['violet'][0], rx=12, dash='6 4')
        f.para(42, fy + 26, 'Tested before training: a fixed suite of deliberate shortcut programs (typical values, wrong '
               'body part, wrong units, clip length only and others) must fail, and the expert pipeline\u2019s own code must pass.',
               1210, 13, INK2)
    f.save(f'{OUT}/fig_check_{variant}.svg')


# ---------------------------------------------------------------- teacher
def fig_teacher():
    f = Fig(1300, 490, 'The privileged teacher',
            'A large teacher model sees the three-camera reference panel but acts only through the student’s tools. '
            'Its runs are filtered and stripped of the panel before the student is fine-tuned on them.')
    f.card(24, 40, 260, 130, 'white', 'Same inputs as the student', ['one-camera video, task text, the same cached tools'])
    f.card(24, 196, 260, 150, 'orange', 'Reference panel (training videos only)',
           ['three-camera joint-angle and center-of-mass curves, and the reference feature values'], dash='6 4')
    f.card(330, 100, 250, 180, 'violet', 'Teacher model', ['Qwen3-VL-235B, frozen. The panel helps it find where the one-camera tools went wrong; it acts only through the student’s tools.'])
    f.arrow([(286, 105), (326, 150)], S)
    f.arrow([(286, 270), (326, 230)], C['orange'][0], dash='6 4')
    f.arrow([(582, 190), (622, 190)], S)
    f.rect(626, 40, 340, 306, fill=PANEL, stroke=RULE, rx=12)
    f.text(644, 70, 'Keep a demonstration only if', 15, INK, 700)
    filt = ['every submitted feature passes the same check as the student’s',
            'its feature code is at least as accurate as the expert pipeline on five other videos of the task',
            'after the panel is removed, no remaining text refers to it']
    yy = 100
    for k, t in enumerate(filt):
        f.check(656, yy + 8, 10)
        yy = f.para(676, yy + 13, t, 270, 13, INK2) + 16
    f.arrow([(968, 190), (1008, 190)], S)
    f.card(1012, 100, 264, 180, 'blue', 'Student', ['Qwen3-VL-8B, fine-tuned with LoRA on the kept demonstrations (at most 40 per task). Never sees the panel.'])
    f.rect(24, 380, 1252, 86, fill=WHITE, stroke=RULE, rx=12)
    f.text(44, 408, 'Comparison arm', 13.5, INK, 700)
    f.para(44, 430, 'A plain teacher (the same model, without the panel) goes through the same filters with the same '
           'number of attempts. Comparing the two warm starts shows what the panel adds.', 1200, 13, INK2)
    f.save(f'{OUT}/fig_teacher.svg')


# ---------------------------------------------------------------- frame shuffle (v4)
def fig_shuffle():
    f = Fig(1300, 420, 'Destroying motion while keeping appearance',
            'The same frames in their true order and shuffled. Appearance is identical; only the motion is destroyed. '
            'A method that measures movement must change its answer; one that reads appearance will not.')
    order = ['flat', 'flat', 'toes', 'toes', 'toes', 'toes', 'flat', 'flat']
    shuf = [3, 6, 0, 5, 1, 7, 2, 4]
    for row, (lab, seq) in enumerate([('true order', list(range(8))), ('shuffled', shuf)]):
        y = 50 + row * 150
        f.text(24, y + 66, lab, 13.5, INK, 700)
        for k, idx in enumerate(seq):
            x = 130 + k * 92
            up = order[idx] == 'toes'
            f.rect(x, y, 80, 120, fill=C['blue'][1] if up else PANEL, stroke=C['blue'][0] if up else RULE, rx=8)
            f.line(x + 6, y + 112, x + 74, y + 112, MUTED, 1.5)
            f.line(x + 6, y + 22, x + 74, y + 22, '#9aa3af', 1, '3 3')
            f.person(x + 40, y + (10 if up else 22), 90, INK2, 2, order[idx])
            f.text(x + 40, y + 136, f'frame {idx + 1}', 11, MUTED, anchor='middle')
    f.card(900, 50, 376, 120, 'aqua', 'A method that measures movement', ['Its order-dependent features (speeds, hold time) change or stop passing the check; angles need not change.'])
    f.card(900, 200, 376, 120, 'red', 'A method that reads appearance', ['Its output barely moves: the person, clothing, body shape and age cues are all still there.'])
    f.text(130, 400, 'Shaded frames show the person risen onto the toes (head above the dashed line). Every tool output is recomputed on the shuffled video.', 13, INK2)
    f.save(f'{OUT}/fig_shuffle.svg')


# ---------------------------------------------------------------- time scaling
def fig_timescale():
    f = Fig(1300, 430, 'Slowing a video down as a controlled test',
            'The center-of-mass curve of a rise-to-toes trial at normal speed and slowed to 0.8 times speed, with the '
            'expected change in each feature.')
    ox, oy, W, H = 70, 60, 600, 260
    tmax = 14
    X = lambda t: ox + t / tmax * W
    f.line(ox, oy + H, ox + W, oy + H, MUTED, 1.2)
    f.line(ox, oy, ox, oy + H, MUTED, 1.2)
    for t in range(0, 15, 2):
        f.text(X(t), oy + H + 18, str(t), 12, MUTED, anchor='middle')
    f.text(ox + W, oy + H + 38, 'time (s)', 12.5, INK2, anchor='end')
    f.add(f'<text transform="translate({ox - 22},{oy + H / 2}) rotate(-90)" font-size="14.5" fill="{INK2}" text-anchor="middle">center-of-mass height</text>')

    def curve(scale, color, dash=None):
        pts = []
        for k in range(281):
            t = k / 280 * tmax
            u = t / scale
            v = 1 / (1 + math.exp(-(u - 3.0) * 4)) - 1 / (1 + math.exp(-(u - 8.0) * 4))
            pts.append((X(t), oy + H - 20 - v * (H - 60)))
        f.path('M' + ' L'.join(f'{a:.1f},{b:.1f}' for a, b in pts), color, 2.6, dash=dash)
    curve(1.0, C['blue'][0])
    curve(1.25, C['orange'][0], '7 5')
    f.line(ox + 20, oy + 8, ox + 50, oy + 8, C['blue'][0], 2.6); f.text(ox + 58, oy + 12, 'original video', 12.5, INK2)
    f.line(ox + 190, oy + 8, ox + 220, oy + 8, C['orange'][0], 2.6, '7 5'); f.text(ox + 228, oy + 12, 'slowed to 0.8× speed', 12.5, INK2)
    x0 = 720
    f.rect(x0, 40, 556, 300, fill=PANEL, stroke=RULE, rx=14)
    f.text(x0 + 20, 70, 'What should happen to each feature', 15, INK, 700)
    rows = [('Hold time', 'longer, ×1.25', 'but never past the 5-second cap: a 4.5 s hold becomes 5 s, not 5.6 s'),
            ('Peak upward speed', 'slower, ×0.8', 'the same rise now takes longer'),
            ('Peak ankle angle', 'unchanged', 'angles do not depend on timing')]
    y = 108
    for n, eff, why in rows:
        f.text(x0 + 20, y, n, 14, INK, 700)
        f.text(x0 + 210, y, eff, 14, INK, 700)
        f.para(x0 + 210, y + 22, why, 320, 12.5, INK2)
        y += 76
    f.para(24, 384, 'Frames are resampled and timestamps corrected, so the person looks identical and only the speed of the movement changes. '
           'A method that measures movement should respond as predicted; a method that reads appearance should not.', 1250, 13, INK2)
    f.save(f'{OUT}/fig_timescale.svg')


# ---------------------------------------------------------------- tool-outcome model
def fig_worldmodel():
    f = Fig(1300, 470, 'A model of what each tool will deliver',
            'Cheap signals feed a tool-outcome model that predicts, for each tool route, the likely feature error, the '
            'chance of failure and the GPU cost, before the expensive call is made.')
    f.rect(24, 40, 300, 300, fill=PANEL, stroke=RULE, rx=12)
    f.text(42, 70, 'Cheap signals (seconds)', 15, INK, 700)
    for k, t in enumerate(['2D pose confidence per joint', 'share of frames with both feet visible', 'person height in pixels',
                           'clip length', 'overall amount of motion', 'which task this is']):
        f.circle(48, 100 + k * 38, 4, fill=INK2, stroke=INK2)
        f.text(62, 105 + k * 38, t, 13, INK2)
    f.arrow([(326, 190), (366, 190)], S)
    f.card(370, 90, 270, 200, 'violet', 'Tool-outcome model', ['Gradient-boosted trees. Learned from development videos, where running each tool and comparing with the three-camera answer gives the true error.'])
    f.arrow([(642, 190), (682, 190)], S)
    f.rect(686, 40, 590, 300, fill=WHITE, stroke=RULE, rx=12)
    f.text(704, 70, 'Predicted for this clip and the feature "peak upward speed"', 14, INK, 700)
    hdr = ['route', 'likely error', 'fails', 'GPU time']
    xs = [704, 930, 1060, 1160]
    for h, x in zip(hdr, xs):
        f.text(x, 104, h, 12.5, MUTED, 600)
    data = [('2D pose + tracking', '0.12', '2%', '10 s'), ('3D reconstruction', '0.05', '9%', '230 s')]
    for j, row in enumerate(data):
        y = 140 + j * 44
        f.rect(700, y - 26, 560, 38, fill=PANEL if j == 0 else C['violet'][1], stroke=RULE, rx=8, sw=1)
        for v, x in zip(row, xs):
            f.text(x, y - 2, v, 13.5, INK, 600 if x == 704 else 400)
    f.para(704, 250, 'The agent can call predict_outcome before deciding whether a four-minute reconstruction is worth it. '
           'The predictions describe the expert pipeline’s route; how well they flag errors in the agent’s own features is tested separately.', 550, 13, INK2)
    f.rect(24, 364, 1252, 82, fill=WHITE, stroke=C['orange'][0], rx=12, dash='6 4')
    f.text(42, 392, 'Where the training labels come from', 14, INK, 700)
    f.para(42, 416, 'For every development video and every cached tool setting, the expert pipeline’s feature code is run on that '
           'tool’s output and compared with the three-camera reference. That error, and whether the call failed, is the label.', 1210, 13, INK2)
    f.save(f'{OUT}/fig_worldmodel.svg')


# ---------------------------------------------------------------- budget (v4)
def fig_budget():
    f = Fig(1100, 440, 'Comparing methods at equal compute',
            'Illustration of the continuation control: the new stage is compared with spending the same extra compute '
            'on the stage before it. The values are made up to show the design.')
    ox, oy, W, H = 90, 70, 640, 280
    f.text(24, 40, 'Illustration of the design, not results', 15, INK, 700)
    budgets = [50, 200, 800]
    X = lambda b: ox + (math.log(b) - math.log(40)) / (math.log(1000) - math.log(40)) * W
    Y = lambda v: oy + H - (v - 0.25) / (0.55 - 0.25) * H
    for v in [0.3, 0.4, 0.5]:
        f.line(ox, Y(v), ox + W, Y(v), '#eceef1', 1)
        f.text(ox - 10, Y(v) + 4, f'{v:.1f}', 12, MUTED, anchor='end')
    for b in budgets:
        f.text(X(b), oy + H + 20, str(b), 12, MUTED, anchor='middle')
    f.line(ox, oy + H, ox + W, oy + H, MUTED, 1.2)
    f.text(ox + W / 2, oy + H + 44, 'development compute (H100-hours, log scale)', 12.5, INK2, anchor='middle')
    f.add(f'<text transform="translate({ox - 50},{oy + H / 2}) rotate(-90)" font-size="14.5" fill="{INK2}" text-anchor="middle">rank agreement</text>')
    lines = [('previous method, continued (control)', '#8a94a3', [0.31, 0.35, 0.37]),
             ('previous method + new stage', C['blue'][0], [0.31, 0.39, 0.46])]
    for name, col, vals in lines:
        pts = [(X(b), Y(v)) for b, v in zip(budgets, vals)]
        f.path('M' + ' L'.join(f'{a:.1f},{c:.1f}' for a, c in pts), col, 2.4)
        for a, c in pts:
            f.circle(a, c, 6, fill=col, stroke=WHITE, sw=2)
        f.text(pts[-1][0] + 12, pts[-1][1] + 4, name, 12.5, INK2)
    xg = X(800)
    f.path(f'M{xg - 14:.1f},{Y(0.37):.1f} H{xg - 24:.1f} V{Y(0.46):.1f} H{xg - 14:.1f}', INK, 1.5)
    f.text(xg - 32, 225, 'gain at equal cost', 12.5, INK, 700, 'end')
    f.save(f'{OUT}/fig_budget.svg')


if __name__ == '__main__':
    for v in ['v1', 'v2', 'v3', 'v5', 'v7']:
        fig_split(v)
    fig_bootstrap(True); fig_bootstrap(False)
    for v in ['v2', 'v4', 'v5', 'v6', 'v7']:
        fig_stages(v)
    fig_cancel()
    for v in ['v3', 'v4', 'v5', 'v7']:
        fig_check(v)
    fig_teacher(); fig_shuffle(); fig_timescale(); fig_worldmodel(); fig_budget()
    print('ok')
