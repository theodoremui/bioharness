"""Heuristic clutter check for figures drawn with svglib.

Estimates text bounding boxes from font size and string length, then reports
(1) overlapping text boxes, (2) text that leaves the canvas, (3) straight line or
polyline segments that pass through a text box, and (4) figures with too many words.

Usage: python3 -B output/idea-summaries-build/lint_svg.py file1.svg [file2.svg ...]
Exit status is 0 even when warnings are printed; read the report.
"""
import re, sys, html

TXT = re.compile(r'<text x="([\d.\-]+)" y="([\d.\-]+)" font-size="([\d.]+)" font-weight="(\d+)"[^>]*?text-anchor="(\w+)"[^>]*>(.*?)</text>')
LINE = re.compile(r'<line x1="([\d.\-]+)" y1="([\d.\-]+)" x2="([\d.\-]+)" y2="([\d.\-]+)"')
PATH = re.compile(r'<path d="([^"]+)"')
TXT_TAG = re.compile(r'<text\b[^>]*>')


def box(x, y, size, weight, anchor, s):
    w = len(s) * size * (0.565 if weight >= 600 else 0.53)
    if anchor == 'middle':
        x0 = x - w / 2
    elif anchor == 'end':
        x0 = x - w
    else:
        x0 = x
    return (x0, y - size * 0.8, x0 + w, y + size * 0.22)


def inter(a, b, pad=1.0):
    return not (a[2] <= b[0] + pad or b[2] <= a[0] + pad or a[3] <= b[1] + pad or b[3] <= a[1] + pad)


def seg_hits_box(p, q, b):
    # sample along the segment
    for i in range(41):
        t = i / 40
        x = p[0] + (q[0] - p[0]) * t
        y = p[1] + (q[1] - p[1]) * t
        if b[0] + 1 < x < b[2] - 1 and b[1] + 1 < y < b[3] - 1:
            return True
    return False


def bez(p0, ps, n=12):
    """Sample a quadratic or cubic Bezier curve."""
    pts = [p0] + ps
    out = []
    for i in range(1, n + 1):
        t = i / n
        q = pts[:]
        while len(q) > 1:
            q = [((1 - t) * a[0] + t * b[0], (1 - t) * a[1] + t * b[1]) for a, b in zip(q, q[1:])]
        out.append(q[0])
    return out


def path_polylines(d):
    """Return a list of polylines (lists of points) for an SVG path, flattening curves.
    Arcs are approximated by the chord between their endpoints and counted in `approx`."""
    toks = re.findall(r'[MmLlHhVvCcQqSsTtAaZz]|-?\d*\.?\d+(?:e-?\d+)?', d)
    polys, cur, start, i, cmd, approx = [], (0.0, 0.0), (0.0, 0.0), 0, None, 0
    poly = []
    def num():
        nonlocal i
        v = float(toks[i]); i += 1; return v
    while i < len(toks):
        if re.match(r'[A-Za-z]', toks[i]):
            cmd = toks[i]; i += 1
            if cmd in 'Zz':
                if poly:
                    poly.append(start); polys.append(poly); poly = []
                cur = start
                continue
        if cmd is None:
            i += 1; continue
        rel = cmd.islower(); c = cmd.upper()
        try:
            if c == 'M':
                x, y = num(), num()
                cur = (cur[0] + x, cur[1] + y) if rel else (x, y)
                if poly: polys.append(poly)
                poly = [cur]; start = cur
                cmd = 'l' if rel else 'L'
            elif c == 'L' or c == 'T':
                x, y = num(), num()
                cur = (cur[0] + x, cur[1] + y) if rel else (x, y); poly.append(cur)
            elif c == 'H':
                x = num(); cur = (cur[0] + x if rel else x, cur[1]); poly.append(cur)
            elif c == 'V':
                y = num(); cur = (cur[0], cur[1] + y if rel else y); poly.append(cur)
            elif c in 'CSQ':
                k = {'C': 3, 'S': 2, 'Q': 2}[c]
                ps = []
                for _ in range(k):
                    x, y = num(), num()
                    ps.append((cur[0] + x, cur[1] + y) if rel else (x, y))
                if c == 'S':
                    ps = [ps[0]] + ps
                poly += bez(cur, ps); cur = ps[-1]
            elif c == 'A':
                for _ in range(5): num()
                x, y = num(), num()
                cur = (cur[0] + x, cur[1] + y) if rel else (x, y); poly.append(cur); approx += 1
            else:
                i += 1
        except (IndexError, ValueError):
            break
    if poly: polys.append(poly)
    return polys, approx


def lint(path):
    src = open(path).read()
    m = re.search(r'viewBox="0 0 ([\d.]+) ([\d.]+)"', src)
    W, H = float(m.group(1)), float(m.group(2))
    texts = []
    for x, y, fs, fw, an, s in TXT.findall(src):
        s = html.unescape(re.sub('<[^>]+>', '', s))
        texts.append((s, box(float(x), float(y), float(fs), int(fw), an, s)))
    issues = []
    for i in range(len(texts)):
        for j in range(i + 1, len(texts)):
            if inter(texts[i][1], texts[j][1]):
                issues.append(f'overlap: "{texts[i][0][:40]}" <> "{texts[j][0][:40]}"')
    for s, b in texts:
        if b[0] < 4 or b[1] < 2 or b[2] > W - 4 or b[3] > H - 2:
            issues.append(f'off-canvas: "{s[:50]}"')
    segs = [((float(a), float(b_)), (float(c), float(d))) for a, b_, c, d in LINE.findall(src)]
    arcs = 0
    for d in PATH.findall(src):
        polys, a = path_polylines(d)
        arcs += a
        for pts in polys:
            segs += list(zip(pts, pts[1:]))
    rotated = sum(1 for t in TXT_TAG.findall(src) if 'transform=' in t)
    if '<g transform="translate' in src and 'rotate(' in src:
        issues.append('coverage: a group uses rotate(); rotated elements are checked at unrotated positions, inspect the PNG')
    if rotated:
        issues.append(f'coverage: {rotated} text element(s) carry a transform and are checked at unrotated positions, inspect the PNG')
    if arcs:
        issues.append(f'coverage: {arcs} arc command(s) approximated by chords')
    for s, b in texts:
        hits = sum(1 for p, q in segs if seg_hits_box(p, q, b))
        if hits:
            issues.append(f'line-through-text ({hits}): "{s[:50]}"')
    words = sum(len(s.split()) for s, _ in texts)
    if words > 120:
        issues.append(f'heavy-text: {words} words (aim for <= 90)')
    print(f'== {path}: {len(texts)} text items, {words} words, {len(issues)} warnings')
    for it in issues:
        print('   ' + it)


if __name__ == '__main__':
    for p in sys.argv[1:]:
        lint(p)
