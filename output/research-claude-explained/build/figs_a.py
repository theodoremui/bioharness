import math, sys
from svglib import *

OUT = sys.argv[1]
S = C['slate'][0]


def fig_chain():
    f = Fig(1300, 470, 'From one video to a task score',
            'Five steps for the rise-to-toes task: video, body landmarks, 3D skeleton and center of mass, three '
            'features in physical units, and rescaling and averaging into a task score of 0.77.')
    xs = [24, 278, 532, 786, 1040]
    W, Y, H = 236, 24, 312
    titles = ['1  Video', '2  Body landmarks', '3  3D body motion', '4  Features', '5  Rescale, average']
    bodies = ['One smartphone records the person at 60 frames per second.',
              'A pose model marks joints such as ankles, knees and hips in every frame.',
              'A reconstruction step turns the landmarks into joint angles and the path of the center of mass.',
              'Code reduces the curves to the few numbers the task asks for.',
              'Each feature is rescaled to 0–1 and the three are averaged into the task score.']
    for i, x in enumerate(xs):
        f.rect(x, Y, W, H, fill=PANEL, stroke=RULE, rx=12)
        f.text(x + 14, Y + 28, titles[i], 15, INK, 700)
        f.para(x + 14, Y + 228, bodies[i], W - 28, 12.5, INK2)
        if i < 4:
            f.arrow([(x + W + 2, Y + 120), (xs[i + 1] - 4, Y + 120)], S)
    # 1 video: phone frame with person
    x = xs[0]
    f.rect(x + 58, Y + 48, 120, 140, fill=WHITE, stroke=INK2, rx=14, sw=2)
    f.person(x + 118, Y + 66, 100, INK2, 2.4, 'toes')
    # 2 landmarks
    x = xs[1]
    f.person(x + 118, Y + 58, 120, '#9aa3af', 2.2, 'toes', dots=True)
    # 3 COM curve
    x = xs[2]
    ox, oy, gw, gh = x + 30, Y + 64, 180, 112
    f.line(ox, oy + gh, ox + gw, oy + gh, MUTED, 1.2)
    f.line(ox, oy, ox, oy + gh, MUTED, 1.2)
    pts = []
    for k in range(61):
        t = k / 60
        h = 1 / (1 + math.exp(-(t - 0.25) * 40)) - 1 / (1 + math.exp(-(t - 0.85) * 40))
        pts.append((ox + t * gw, oy + gh - 10 - h * (gh - 30)))
    f.path('M' + ' L'.join(f'{a:.1f},{b:.1f}' for a, b in pts), C['blue'][0], 2.5)
    f.text(ox + 4, oy - 8, 'center-of-mass height', 11.5, MUTED)
    f.text(ox + gw, oy + gh + 15, 'time', 11.5, MUTED, anchor='end')
    f.line(ox + 0.25 * gw, oy + gh - 10, ox + 0.25 * gw, oy + 20, C['orange'][0], 1.3, '4 3')
    f.text(ox + 0.25 * gw - 5, oy + 34, 'rise', 11.5, C['orange'][2], anchor='end')
    # 4 features
    x = xs[3]
    rows = [('peak rise speed', '0.30 m/s'), ('peak ankle angle', '36°'), ('hold time', '5.0 s')]
    for j, (a, b) in enumerate(rows):
        yy = Y + 62 + j * 44
        f.rect(x + 14, yy, W - 28, 34, fill=WHITE, stroke=RULE, rx=8)
        f.text(x + 22, yy + 22, a, 12, INK2)
        f.text(x + W - 24, yy + 22, b, 13.5, INK, 700, 'end')
    # 5 rescale
    x = xs[4]
    vals = [0.55, 0.75, 1.00]
    for j, v in enumerate(vals):
        yy = Y + 66 + j * 34
        f.rect(x + 14, yy, 150, 14, fill=WHITE, stroke=RULE, rx=4, sw=1)
        f.rect(x + 14, yy, 150 * v, 14, fill=C['blue'][0], stroke=C['blue'][0], rx=4, sw=1)
        f.text(x + 174, yy + 12, f'{v:.2f}', 13, INK, 600)
    f.line(x + 14, Y + 170, x + W - 14, Y + 170, RULE, 1.2)
    f.text(x + 14, Y + 196, 'task score', 13, INK2)
    f.text(x + W - 14, Y + 197, '0.77', 18, INK, 700, 'end')
    # formula strip
    f.rect(24, 354, 1252, 94, fill=WHITE, stroke=RULE, rx=12)
    f.text(44, 382, 'Rescaling one feature', 14, INK, 700)
    f.text(44, 408, 'rescaled value = (value − lowest value in the data) ÷ (highest value − lowest value)', 14, INK2)
    f.text(44, 433, 'speed: (0.30 − 0.03) ÷ (0.52 − 0.03) = 0.55', 13, INK2)
    f.text(480, 433, 'ankle: (36 − (−6)) ÷ (50 − (−6)) = 0.75', 13, INK2)
    f.text(880, 433, 'hold: (5.0 − 0.2) ÷ (5.0 − 0.2) = 1.00', 13, INK2)
    f.save(f'{OUT}/fig_chain.svg')


def fig_cameras():
    f = Fig(1300, 470, 'Three cameras versus one camera',
            'Left: with three cameras the lines of sight cross at a single point, so the 3D position is fixed. '
            'Right: with one camera every point along one line of sight lands on the same pixel, so depth must be guessed.')
    for x0, title in [(24, 'A   Three phones: lines of sight cross at one point'),
                      (662, 'B   One phone: many depths give the same picture')]:
        f.rect(x0, 24, 614, 422, fill=PANEL, stroke=RULE, rx=14)
        f.text(x0 + 22, 56, title, 16, INK, 700)
    # A
    P = (440, 230)
    cams = [(100, 120, 0), (90, 300, 0), (250, 365, 0)]
    for cx, cy, ang in cams:
        dx, dy = P[0] - cx, P[1] - cy
        L = math.hypot(dx, dy)
        ux, uy = dx / L, dy / L
        f.line(cx + ux * 24, cy + uy * 24, P[0] + ux * 36, P[1] + uy * 36, C['blue'][0], 2)
        f.camera(cx, cy, 1.3, INK2, math.degrees(math.atan2(dy, dx)))
    f.circle(P[0], P[1], 9, fill=C['orange'][0], stroke=WHITE, sw=2)
    f.text(P[0] + 50, P[1] - 4, 'ankle', 14, INK, 700)
    f.text(P[0] + 50, P[1] + 14, 'one possible position', 12.5, INK2)
    f.para(46, 408, 'Geometry fixes the 3D position (triangulation), the way two eyes judge distance.', 560, 13, INK2)
    # B
    cx, cy = 730, 250
    f.camera(cx, cy, 1.3, INK2, -8)
    ex, ey = 1250, 177
    f.line(cx + 22, cy - 3, ex, ey, C['blue'][0], 2)
    # image plane
    f.line(790, 205, 790, 270, INK2, 2.5)
    f.text(800, 296, 'image', 12, MUTED)
    f.circle(790, 241.6, 5, fill=C['orange'][0], stroke=WHITE, sw=1.5)
    for t, hh, lab in [(0.33, 46, 'near, small'), (0.6, 84, 'middle'), (0.88, 124, 'far, large')]:
        px, py = cx + 22 + t * (ex - cx - 22), cy - 3 + t * (ey - cy + 3)
        f.person(px, py - hh * 0.55, hh, '#9aa3af', 2)
        f.circle(px, py, 6, fill=C['orange'][0], stroke=WHITE, sw=1.5)
        f.text(px, py + hh * 0.45 + 22, lab, 12.5, INK2, anchor='middle')
    f.para(684, 408, 'Every point on this line lands on the same pixel. Depth has to be inferred from learned body shape and motion.', 570, 13, INK2)
    f.save(f'{OUT}/fig_cameras.svg')


def fig_routes():
    f = Fig(1300, 500, 'Three ways to get a balance score from video',
            'Reconstruct and measure, learn to predict, and learn to conduct the analysis with a tool-calling agent, '
            'each with its main strength and weakness.')
    lanes = [
        ('Reconstruct and measure', 'slate',
         [('Video', 90), ('3D skeleton from one camera', 200), ('StaBLE rules compute features', 200), ('Score', 80)],
         ['+ every step can be plotted and checked', '− if one step fails there is no score; minutes of GPU time per clip']),
        ('Learn to predict', 'slate',
         [('Video', 90), ('Neural network trained on scores', 400), ('Score', 80)],
         ['+ always returns a number', '− cannot show where the number came from; close to a constant guess']),
        ('Learn to conduct the analysis', 'blue',
         [('Video + task text', 120), ('VLM agent ⇄ tools', 182), ('Features + code', 118), ('Fixed formula → score', 150)],
         ['+ every number traces to a measurement', '+ can switch tools when one fails', '? must learn to choose and check tools']),
    ]
    y = 24
    for name, role, boxes, notes in lanes:
        hl = role == 'blue'
        f.rect(24, y, 1252, 142, fill=C['blue'][1] if hl else PANEL, stroke=C['blue'][0] if hl else RULE, rx=14,
               sw=2 if hl else 1.5)
        f.text(44, y + 34, name, 16, INK, 700)
        if hl:
            f.pill(44, y + 48, 'this proposal', 'blue', 11)
        x = 240
        for i, (b, w) in enumerate(boxes):
            r = 'blue' if (hl and 'agent' in b) else 'white'
            f.rect(x, y + 54, w, 58, fill=C[r][1], stroke=C[r][0], rx=10)
            f.para(x + w / 2, y + 78 if tw(b, 13.5) > w - 20 else y + 88, b, w - 18, 13.5, INK, weight=600, anchor='middle')
            if i < len(boxes) - 1:
                f.arrow([(x + w + 2, y + 83), (x + w + 22, y + 83)], S)
            x += w + 26
        ny = y + 52
        for j, n in enumerate(notes):
            ny = f.para(912, ny, n.strip(), 350, 12.5, INK2) + 2
        y += 158
    f.save(f'{OUT}/fig_routes.svg')


def fig_pilot():
    rows = [('Qwen3-VL-8B fine-tuned to output scores', 0.100, 'blue', ''),
            ('2D pose (RTMPose) + temporal network', 0.119, 'blue', ''),
            ('Constant guess: each task’s training average', 0.120, 'slate', 'uses no video'),
            ('OpenCap Monocular + StaBLE rules', 0.146, 'blue', 'error over its 567 valid cases only'),
            ('Qwen3-VL-8B asked for features, score by formula', 0.179, 'blue', ''),
            ('Qwen3-VL-8B asked for a score, no training', 0.238, 'blue', '')]
    f = Fig(1300, 430, 'Pilot results on 43 held-out participants',
            'Task-averaged mean absolute error for six methods. The fine-tuned model scores 0.100, the constant '
            'guess 0.120 and the untrained model 0.238.')
    L, R, top, rh = 450, 1120, 60, 50
    sc = (R - L) / 0.25
    f.text(24, 36, 'Task-averaged mean absolute error, 43 test participants (lower is better)', 15, INK, 700)
    for k in range(6):
        v = k * 0.05
        x = L + v * sc
        f.line(x, top - 6, x, top + rh * 6, '#eceef1', 1)
        f.text(x, top + rh * 6 + 22, f'{v:.2f}', 12.5, MUTED, anchor='middle')
    for i, (name, v, role, note) in enumerate(rows):
        y = top + i * rh
        f.text(L - 16, y + 21, name, 13.5, INK, 400, 'end')
        col = '#9aa3af' if role == 'slate' else C['blue'][0]
        f.add(f'<path d="M{L},{y + 6} H{L + v * sc - 4} a4,4 0 0 1 4,4 V{y + 26} a4,4 0 0 1 -4,4 H{L} Z" fill="{col}"/>')
        f.text(L + v * sc + 8, y + 23, f'{v:.3f}', 13.5, INK, 700)
        if note:
            f.text(L + v * sc + 62, y + 23, note, 12.5, INK2, italic=True)
    xg = L + 0.120 * sc
    f.line(xg, top - 10, xg, top + rh * 6, INK2, 1.5, '5 4')
    f.text(xg + 6, top - 14, 'constant guess', 12, INK2)
    f.text(24, top + rh * 6 + 48, 'Error = average distance between predicted and reference task scores on the 0–1 scale, per task, then averaged over tasks.', 12.5, MUTED)
    f.save(f'{OUT}/fig_pilot.svg')


def fig_agent_loop():
    f = Fig(1300, 660, 'The agent loop and one example trajectory',
            'Left: the vision-language model writes tool calls; the harness runs the tools and returns results; '
            'the final submission goes through a fixed formula to give the score. Right: an illustrative trajectory for rise to toes.')
    f.text(24, 44, 'A   How the parts connect', 16, INK, 700)
    f.card(24, 70, 250, 210, 'white', 'Inputs', ['Video from one phone', 'Task description', 'Feature definitions with units', 'Height and lens parameters (passed to the tools)'])
    f.card(330, 70, 300, 150, 'blue', 'Vision-language model',
           ['Qwen3-VL-8B. Reads text, video frames and plots; writes the next step as text, which may be a tool call.'])
    f.arrow([(276, 145), (326, 145)], S)
    f.card(330, 320, 300, 150, 'slate', 'Harness (ordinary code)',
           ['Spots a tool call in the text, runs the tool, writes the result back, keeps the transcript and stops at submit.'])
    f.rect(680, 70, 210, 400, fill=WHITE, stroke=RULE, rx=12)
    f.text(696, 100, 'Tools', 15, INK, 700)
    for j, t in enumerate(['frames, crop', 'pose2d', 'segment_person', 'track_points', 'reconstruct3d', 'plot', 'python']):
        f.pill(696, 122 + j * 46, t, 'slate', 12.5)
    f.arrow([(430, 222), (430, 316)], C['blue'][0])
    f.text(420, 258, 'tool call', 12.5, INK2, 600, 'end')
    f.text(420, 276, 'pose2d(video)', 12, INK2, 400, 'end', mono=True)
    f.arrow([(540, 316), (540, 222)], S)
    f.text(550, 258, 'result', 12.5, INK2, 600)
    f.text(550, 276, 'summary or plot', 12, INK2)
    f.arrow([(632, 375), (676, 375)], S)
    f.arrow([(676, 420), (632, 420)], S)
    f.text(654, 365, 'run', 11.5, MUTED, anchor='middle')
    f.text(654, 440, 'output', 11.5, MUTED, anchor='middle')
    f.arrow([(480, 472), (480, 536)], C['blue'][0])
    f.text(490, 510, 'submit', 12.5, INK2, 600)
    f.card(330, 540, 300, 92, 'blue', 'Submission', ['features in physical units, plus the code that computed each one'], tsize=14, bsize=12.5)
    f.card(680, 540, 210, 92, 'white', 'Fixed formula', ['rescale, average: task score'], tsize=14, bsize=12.5)
    f.arrow([(632, 586), (676, 586)], S)
    x0 = 930
    f.rect(x0, 24, 346, 612, fill=PANEL, stroke=RULE, rx=14)
    f.text(x0 + 18, 56, 'B   One trajectory (illustrative)', 16, INK, 700)
    steps = [('model', 'pose2d(video)'), ('harness', '26 landmarks per frame; ankles visible in 98% of frames'),
             ('model', 'plot(heel_height)'), ('harness', '[image of the curve: rise near 4.1 s, return near 10.3 s]'),
             ('model', 'mark task_start = 3.9 s, task_end = 10.6 s'), ('model', 'reconstruct3d(video)'),
             ('harness', 'joint-angle and center-of-mass curves'),
             ('model', 'python: fastest upward center-of-mass speed between the marks'), ('harness', '0.31 m/s'),
             ('model', 'submit(three features + their code)')]
    y = 96
    for who, t in steps:
        role = 'blue' if who == 'model' else 'slate'
        f.pill(x0 + 18, y - 15, who, role, 11)
        mono = who == 'model' and ('(' in t or '=' in t) and not t.startswith('python')
        y = f.para(x0 + 100, y, t, 228, 12.5, INK if who == 'model' else INK2, mono=mono) + 16
    f.save(f'{OUT}/fig_agent_loop.svg')


def fig_levers():
    f = Fig(1300, 446, 'Four ways to improve an agent',
            'An agent is made of model weights, a prompt and harness code. Prompt optimization edits the prompt, '
            'harness search edits the harness code, and supervised fine-tuning and reinforcement learning change the weights.')
    f.rect(24, 24, 1252, 110, fill=PANEL, stroke=RULE, rx=14)
    f.text(44, 56, 'An agent is three things', 16, INK, 700)
    parts = [('Prompt', 'instructions and tool descriptions (text)', 'yellow', 300),
             ('Harness code', 'retry rules, tool defaults, checks', 'slate', 640),
             ('Model weights', 'billions of numbers inside the network', 'blue', 980)]
    for name, sub, role, x in parts:
        f.rect(x - 130, 70, 260, 50, fill=C[role][1], stroke=C[role][0], rx=10)
        f.text(x, 92, name, 14.5, INK, 700, 'middle')
        f.text(x, 110, sub, 12, INK2, anchor='middle')
    cols = [('1  Prompt optimization', 'yellow', 300, 'e.g. GEPA',
             'A second language model reads logs of failed runs and rewrites the instructions. Rewrites that score better on training examples are kept.',
             'Cost: model runs, no training'),
            ('2  Harness search', 'slate', 640, 'e.g. Meta-Harness',
             'A proposer model edits the harness code and keeps a record of every version it tried and how well it did.',
             'Cost: model runs, no training'),
            ('3  Supervised fine-tuning', 'blue', 980, 'with LoRA adapters',
             'Show the model good example runs and nudge its weights so those runs become more likely.',
             'Cost: GPU training'),
            ('4  Reinforcement learning', 'blue', 980, 'with GRPO',
             'Let the model try several runs, score each with a reward, and nudge the weights toward the better ones.',
             'Cost: most GPU time')]
    xs = [24, 340, 656, 972]
    for (title, role, tx, sub, body, cost), x in zip(cols, xs):
        f.rect(x, 176, 304, 246, fill=WHITE, stroke=C[role][0], rx=14, sw=1.6)
        f.text(x + 18, 208, title, 15.5, INK, 700)
        f.text(x + 18, 230, sub, 12.5, MUTED, italic=True)
        f.para(x + 18, 262, body, 268, 13, INK2)
        f.pill(x + 18, 382, cost, role, 11.5)
        f.arrow([(x + 152, 172), (tx, 124)], C[role][0] if role != 'yellow' else C['yellow'][2], 1.6)
    f.save(f'{OUT}/fig_levers.svg')


def fig_grpo():
    r = [-0.05, -0.12, -0.30, -0.08, -0.20, -0.10, -0.40, -0.07]
    m = sum(r) / len(r)
    sd = (sum((x - m) ** 2 for x in r) / len(r)) ** 0.5
    A = [(x - m) / sd for x in r]
    f = Fig(1300, 520, 'Group relative policy optimization in one picture',
            'Eight attempts on the same video receive rewards. Each reward is compared with the group average; '
            'above-average attempts get positive advantages and are made more likely.')
    f.card(24, 150, 190, 150, 'white', 'One training video', ['rise to toes, participant 17'])
    f.card(250, 150, 190, 150, 'blue', 'Agent', ['samples 8 complete attempts at the same task'])
    f.arrow([(216, 225), (246, 225)], S)
    f.text(480, 40, 'Attempt', 13, MUTED, 600)
    f.text(640, 40, 'Reward', 13, MUTED, 600, 'end')
    f.text(900, 40, 'Advantage = (reward − group average) ÷ group spread', 13, MUTED, 600, 'middle')
    cx, s = 900, 85
    for i, (ri, ai) in enumerate(zip(r, A)):
        y = 58 + i * 46
        f.rect(470, y, 180, 34, fill=PANEL, stroke=RULE, rx=8, sw=1)
        f.text(484, y + 22, f'attempt {i + 1}', 13, INK2)
        f.text(640, y + 22, f'{ri:+.2f}', 13.5, INK, 700, 'end')
        col = C['blue'][0] if ai > 0 else C['orange'][0]
        x1, x2 = (cx, cx + ai * s) if ai > 0 else (cx + ai * s, cx)
        f.rect(x1, y + 6, x2 - x1, 22, fill=col, stroke=col, rx=4, sw=0)
        f.text(cx + ai * s + (8 if ai > 0 else -8), y + 22, f'{ai:+.2f}', 12.5, INK, 600, 'start' if ai > 0 else 'end')
    f.arrow([(442, 225), (466, 225)], S)
    f.line(cx, 50, cx, 58 + 8 * 46, INK2, 1.5)
    f.text(cx, 58 + 8 * 46 + 18, 'group average', 12, INK2, anchor='middle')
    f.text(cx + 150, 58 + 8 * 46 + 18, 'make more likely', 12.5, C['blue'][2], 600, 'middle')
    f.text(cx - 150, 58 + 8 * 46 + 18, 'make less likely', 12.5, C['orange'][2], 600, 'middle')
    f.para(24, 340, f'Group average reward = {m:.3f}. Only the comparison inside the group matters, so no separate '
           f'network is needed to guess how good an attempt "should" be.', 410, 13, INK2)
    f.save(f'{OUT}/fig_grpo.svg')


def fig_guess():
    true = [0.4, 0.5, 0.6, 0.7, 0.8]
    sets = [('Constant guess', [0.6] * 5, 'error 0.120', 'rank agreement: none (all tied)', 'slope 0'),
            ('Shrunk toward the average', [0.56, 0.58, 0.60, 0.62, 0.64], 'error 0.096', 'rank agreement 1.0', 'slope 0.2'),
            ('Noisy but measuring', [0.50, 0.45, 0.70, 0.60, 0.85], 'error 0.080', 'rank agreement 0.8', 'slope 0.85')]
    f = Fig(1300, 556, 'Low error can hide a method that ignores the person',
            'Three predictors for five people with true scores 0.4 to 0.8. The constant guess and the shrunk predictor '
            'have errors close to the noisy measuring predictor, but only the measuring one keeps the differences between people.')
    for k, (title, pred, e, rho, sl) in enumerate(sets):
        x0 = 24 + k * 422
        f.rect(x0, 24, 404, 472, fill=PANEL, stroke=RULE, rx=14)
        f.text(x0 + 20, 54, title, 16, INK, 700)
        if k == 0:
            pass
        ox, oy, W = x0 + 70, 80, 300
        lo, hi = 0.3, 0.9
        X = lambda v: ox + (v - lo) / (hi - lo) * W
        Yv = lambda v: oy + W - (v - lo) / (hi - lo) * W
        for t in [0.4, 0.6, 0.8]:
            f.line(X(t), oy, X(t), oy + W, '#e6e8eb', 1)
            f.line(ox, Yv(t), ox + W, Yv(t), '#e6e8eb', 1)
            f.text(X(t), oy + W + 18, f'{t:.1f}', 12, MUTED, anchor='middle')
            f.text(ox - 8, Yv(t) + 4, f'{t:.1f}', 12, MUTED, anchor='end')
        f.rect(ox, oy, W, W, fill='none', stroke=RULE, rx=0, sw=1)
        f.line(X(lo), Yv(lo), X(hi), Yv(hi), '#9aa3af', 1.5, '6 5')
        mt, mp = sum(true) / 5, sum(pred) / 5
        b = sum((a - mt) * (p - mp) for a, p in zip(true, pred)) / sum((a - mt) ** 2 for a in true)
        f.line(X(0.35), Yv(mp + b * (0.35 - mt)), X(0.85), Yv(mp + b * (0.85 - mt)), C['blue'][2], 2)
        for a, p in zip(true, pred):
            f.circle(X(a), Yv(p), 7, fill=C['blue'][0], stroke=WHITE, sw=2)
        f.text(ox + W / 2, oy + W + 40, 'true score', 12.5, INK2, anchor='middle')
        f.add(f'<text transform="translate({ox - 40},{oy + W / 2}) rotate(-90)" font-size="14.5" fill="{INK2}" '
              f'text-anchor="middle">predicted score</text>')
        f.text(x0 + 20, 450, e, 14, INK, 700)
        f.text(x0 + 140, 450, sl, 14, INK, 700)
        f.text(x0 + 20, 474, rho, 13.5, INK2)
    f.line(40, 527, 70, 527, '#9aa3af', 1.5, '6 5'); f.text(78, 531, 'perfect prediction', 12.5, INK2)
    f.line(240, 527, 270, 527, C['blue'][2], 2); f.text(278, 531, 'straight-line fit (its slope is the calibration slope)', 12.5, INK2)
    f.save(f'{OUT}/fig_guess.svg')


if __name__ == '__main__':
    for fn in [fig_chain, fig_cameras, fig_routes, fig_pilot, fig_agent_loop, fig_levers, fig_grpo, fig_guess]:
        fn()
    print('ok')
