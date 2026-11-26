"""Overview figure for docs/research-overview.md: where proposals 05 to 08 act in a self-improving agent."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from svglib import Fig, C, INK, INK2  # noqa: E402

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
OUT = os.path.join(ROOT, 'docs', 'research-plans', 'images', 'overview')
os.makedirs(OUT, exist_ok=True)


def badge(f, cx, cy, label, role):
    """Numbered disc used for every proposal, so the four read as one set."""
    col = C[role][0]
    f.circle(cx, cy, 19, fill=col, stroke=col, sw=1)
    f.text(cx, cy + 6, label, 14, '#ffffff', 700, 'middle')


def four_interfaces():
    f = Fig(1240, 590, 'Four places where self-improvement can go wrong',
            'A phone video enters an editable harness made of tools, an encoding of tool outputs and a VLM agent, '
            'which reports a balance score. A referral or hypothesis can be given to the agent. Scores on development '
            'people feed an improver that proposes an edit; the candidate is scored, and an acceptance rule keeps or '
            'rejects it. Proposal 05 studies the editable harness code, 06 the acceptance rule, 07 the encoding of '
            'tool outputs and 08 the referral given to the agent.')
    slate, orange, violet = C['slate'], C['orange'], C['violet']

    f.text(40, 48, 'Four places where self-improvement can go wrong', 19, INK, 700)

    # proposal 08: referral given to the agent
    rx, ry, rw, rh = 700, 80, 300, 62
    f.card(rx, ry, rw, rh, 'violet', title='Referral or hypothesis', tsize=16)
    badge(f, rx + rw - 30, ry + rh / 2, '08', 'violet')

    # proposal 05: the editable harness (frame encloses only the code)
    fx, fy, fw, fh = 222, 184, 806, 196
    f.rect(fx, fy, fw, fh, fill='#fbfcfd', stroke=slate[0], rx=16, sw=1.6, dash='7 6')
    f.text(fx + 24, fy + 34, 'Editable harness code', 16, INK, 700)
    badge(f, fx + 24 + 244, fy + 28, '05', 'blue')

    y, h = 246, 104
    f.card(40, y, 140, h, 'white', title='Phone video', tsize=16)
    f.card(242, y, 210, h, 'white', title='Tools', body='Pose and 3D motion', tsize=16, bsize=14)
    f.card(498, y, 220, h, 'aqua', title='Tool-output encoding', body='Text, plot or overlay', tsize=16, bsize=14)
    badge(f, 498 + 220 - 30, y + 30, '07', 'aqua')
    f.card(764, y, 244, h, 'white', title='VLM agent', body='Reads the encoded outputs', tsize=16, bsize=14)
    f.card(1070, y, 130, h, 'white', title='Balance score', tsize=16)
    for x1, x2 in [(180, 242), (452, 498), (718, 764), (1008, 1070)]:
        f.arrow([(x1 + 4, y + h / 2), (x2 - 6, y + h / 2)], color=slate[0], sw=2)
    f.arrow([(886, ry + rh + 4), (886, y - 6)], color=violet[0], sw=2.2)

    # improvement loop, right to left; proposal 06 is the acceptance rule
    ly, lh = 456, 96
    f.card(950, ly, 250, lh, 'white', title='Current harness scores', body='Dev people, by group', tsize=16, bsize=14)
    f.card(660, ly, 250, lh, 'white', title='Improver proposes', body='An edit to the code', tsize=16, bsize=14)
    f.card(370, ly, 250, lh, 'white', title='Score the candidate', body='Same dev people', tsize=16, bsize=14)
    f.card(40, ly, 290, lh, 'orange', title='Edit acceptance rule', body='Keeps or rejects it', tsize=16, bsize=14)
    badge(f, 40 + 290 - 30, ly + 30, '06', 'orange')
    f.arrow([(1135, y + h + 4), (1135, ly - 6)], color=slate[0], sw=2)
    for x1, x2 in [(950, 910), (660, 620), (370, 330)]:
        f.arrow([(x1 - 4, ly + lh / 2), (x2 + 6, ly + lh / 2)], color=slate[0], sw=2)
    f.arrow([(290, ly - 4), (290, 420), (475, 420), (475, fy + fh + 6)], color=orange[0], sw=2.2)
    f.text(490, 412, 'accepted edits', 14, C['orange'][2], 600)

    f.save(os.path.join(OUT, 'four-interfaces.svg'))


if __name__ == '__main__':
    four_interfaces()
    print('ok')
