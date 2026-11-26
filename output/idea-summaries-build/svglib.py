"""Small SVG helper used to draw every figure in one consistent style."""
import math

FONT = "Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
MONO = "'SF Mono', Menlo, Consolas, monospace"
INK, INK2, MUTED, RULE, PANEL, WHITE = '#1f2328', '#4b5563', '#6b7280', '#d6d9de', '#f6f7f9', '#ffffff'
# role -> (stroke, fill, dark)
C = {
    'blue':   ('#2a78d6', '#eaf2fc', '#1c5cab'),
    'orange': ('#eb6834', '#fdf0e9', '#b9461a'),
    'aqua':   ('#1baf7a', '#e6f6f0', '#11805a'),
    'red':    ('#e34948', '#fdeded', '#b42d2c'),
    'violet': ('#6250d6', '#f0eefc', '#4a3aa7'),
    'slate':  ('#64748b', '#f3f4f6', '#334155'),
    'yellow': ('#eda100', '#fdf6e3', '#946400'),
    'white':  ('#d6d9de', '#ffffff', '#334155'),
}


FS = 1.18  # global text scale so labels stay legible when a 1300-px figure is shown ~850 px wide


def esc(s):
    return str(s).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def tw(s, size, weight=400):
    return len(s) * size * FS * (0.565 if weight >= 600 else 0.53)


def wrap(text, width, size, weight=400):
    out = []
    for para in str(text).split('\n'):
        cur = ''
        for w in para.split():
            t = (cur + ' ' + w).strip()
            if tw(t, size, weight) <= width or not cur:
                cur = t
            else:
                out.append(cur)
                cur = w
        out.append(cur)
    return out


class Fig:
    def __init__(self, w, h, title, desc):
        self.w, self.h, self.title, self.desc = w, h, title, desc
        self.items, self.markers = [], {}

    def add(self, s):
        self.items.append(s)

    # primitives -------------------------------------------------------
    def rect(self, x, y, w, h, fill=WHITE, stroke=RULE, rx=12, sw=1.5, dash=None, opacity=None):
        d = f' stroke-dasharray="{dash}"' if dash else ''
        o = f' opacity="{opacity}"' if opacity is not None else ''
        self.add(f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx}" fill="{fill}" '
                 f'stroke="{stroke}" stroke-width="{sw}"{d}{o}/>')

    def text(self, x, y, t, size=14, fill=INK, weight=400, anchor='start', italic=False, mono=False):
        st = ' font-style="italic"' if italic else ''
        fam = f' font-family="{MONO}"' if mono else ''
        self.add(f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size * FS:.1f}" font-weight="{weight}" fill="{fill}" '
                 f'text-anchor="{anchor}"{st}{fam}>{esc(t)}</text>')

    def para(self, x, y, t, width, size=13, fill=INK2, lh=None, weight=400, anchor='start', italic=False, mono=False):
        lh = lh or round(size * FS * 1.38, 1)
        lines = wrap(t, width, size * (1.12 if mono else 1.0), weight)
        for i, l in enumerate(lines):
            self.text(x, y + i * lh, l, size, fill, weight, anchor, italic, mono)
        return y + len(lines) * lh

    def line(self, x1, y1, x2, y2, stroke=RULE, sw=1.5, dash=None, cap='round'):
        d = f' stroke-dasharray="{dash}"' if dash else ''
        self.add(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{stroke}" '
                 f'stroke-width="{sw}" stroke-linecap="{cap}"{d}/>')

    def path(self, d, stroke=INK2, sw=2, fill='none', dash=None, cap='round', join='round'):
        da = f' stroke-dasharray="{dash}"' if dash else ''
        self.add(f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" stroke-linecap="{cap}" '
                 f'stroke-linejoin="{join}"{da}/>')

    def circle(self, cx, cy, r, fill=WHITE, stroke=INK2, sw=1.5):
        self.add(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')

    def marker(self, color):
        mid = 'm' + color.strip('#')
        self.markers[mid] = color
        return mid

    def arrow(self, pts, color='#64748b', sw=2, dash=None, head=True):
        d = 'M' + ' L'.join(f'{x:.1f},{y:.1f}' for x, y in pts)
        da = f' stroke-dasharray="{dash}"' if dash else ''
        mk = f' marker-end="url(#{self.marker(color)})"' if head else ''
        self.add(f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{sw}" stroke-linejoin="round"{da}{mk}/>')

    # composite elements ----------------------------------------------
    def card(self, x, y, w, h, role='white', title=None, body=None, tsize=15, bsize=13, pad=14,
             title_fill=INK, body_fill=INK2, dash=None, sw=1.5, tag=None):
        col, bg, dark = C[role]
        self.rect(x, y, w, h, fill=bg, stroke=col, rx=12, sw=sw, dash=dash)
        yy = y + pad + tsize * FS * 0.85
        if tag:
            self.pill(x + pad, y + pad - 2, tag, role, size=11)
            yy += 24
        if title:
            for l in wrap(title, w - 2 * pad, tsize, 700):
                self.text(x + pad, yy, l, tsize, title_fill, 700)
                yy += tsize * FS * 1.3
            yy += 2
        if body:
            items = body if isinstance(body, list) else [body]
            for item in items:
                yy = self.para(x + pad, yy + bsize * 0.15, item, w - 2 * pad, bsize, body_fill) + 3
        return yy

    def pill(self, x, y, t, role='slate', size=12, filled=True, anchor='start', bold=True):
        col, bg, dark = C[role]
        w = tw(t, size, 600) + 18
        if anchor == 'middle':
            x = x - w / 2
        ph = size * FS + 10
        self.rect(x, y, w, ph, fill=bg if filled else WHITE, stroke=col, rx=ph / 2, sw=1.2)
        self.text(x + w / 2, y + ph / 2 + size * FS * 0.36, t, size, dark, 600 if bold else 400, 'middle')
        return w

    def check(self, cx, cy, r=11, ok=True):
        col = C['aqua'][0] if ok else C['red'][0]
        self.circle(cx, cy, r, fill=col, stroke=col, sw=1)
        if ok:
            self.path(f'M{cx - r * 0.45:.1f},{cy + r * 0.02:.1f} L{cx - r * 0.1:.1f},{cy + r * 0.38:.1f} '
                      f'L{cx + r * 0.5:.1f},{cy - r * 0.35:.1f}', stroke=WHITE, sw=2.4)
        else:
            k = r * 0.38
            self.path(f'M{cx - k:.1f},{cy - k:.1f} L{cx + k:.1f},{cy + k:.1f} M{cx + k:.1f},{cy - k:.1f} '
                      f'L{cx - k:.1f},{cy + k:.1f}', stroke=WHITE, sw=2.4)

    def lock(self, x, y, s=1.0, color='#b42d2c'):
        self.path(f'M{x + 4 * s:.1f},{y + 8 * s:.1f} V{y + 5.5 * s:.1f} a{4 * s:.1f},{4 * s:.1f} 0 0 1 {8 * s:.1f},0 '
                  f'V{y + 8 * s:.1f}', stroke=color, sw=1.8 * s)
        self.add(f'<rect x="{x + 1.5 * s:.1f}" y="{y + 8 * s:.1f}" width="{13 * s:.1f}" height="{9 * s:.1f}" '
                 f'rx="{2 * s:.1f}" fill="{color}"/>')

    def person(self, cx, top, h=60, color=INK2, sw=2.2, pose='stand', dots=False, dot_color=None):
        """Stick figure. top = head top y, h = total height."""
        r = h * 0.09
        hy = top + r
        neck = top + 2 * r + h * 0.02
        hip = top + h * 0.55
        foot = top + h
        heel_lift = h * 0.08 if pose == 'toes' else 0
        self.circle(cx, hy, r, fill=WHITE, stroke=color, sw=sw)
        self.line(cx, neck, cx, hip, color, sw)
        self.line(cx, neck + h * 0.08, cx - h * 0.17, hip - h * 0.05, color, sw)
        self.line(cx, neck + h * 0.08, cx + h * 0.17, hip - h * 0.05, color, sw)
        self.line(cx, hip, cx - h * 0.11, foot - heel_lift, color, sw)
        self.line(cx, hip, cx + h * 0.11, foot - heel_lift, color, sw)
        if pose == 'toes':
            self.line(cx - h * 0.11, foot - heel_lift, cx - h * 0.16, foot, color, sw)
            self.line(cx + h * 0.11, foot - heel_lift, cx + h * 0.16, foot, color, sw)
        if dots:
            dc = dot_color or C['orange'][0]
            for (px, py) in [(cx, hy), (cx, neck + h * 0.08), (cx - h * 0.17, hip - h * 0.05),
                             (cx + h * 0.17, hip - h * 0.05), (cx, hip), (cx - h * 0.11, foot - heel_lift),
                             (cx + h * 0.11, foot - heel_lift), (cx - h * 0.055, hip + (foot - hip) / 2),
                             (cx + h * 0.055, hip + (foot - hip) / 2)]:
                self.circle(px, py, max(2.5, h * 0.035), fill=dc, stroke=WHITE, sw=1)

    def camera(self, x, y, s=1.0, color=INK2, angle=0):
        g = f'<g transform="translate({x:.1f},{y:.1f}) rotate({angle}) scale({s})">'
        g += (f'<rect x="-14" y="-10" width="22" height="20" rx="3" fill="{color}"/>'
              f'<path d="M8,-6 L18,-11 L18,11 L8,6 Z" fill="{color}"/></g>')
        self.add(g)

    def save(self, path):
        defs = ''.join(
            f'<marker id="{mid}" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="7" markerHeight="7" '
            f'orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{col}"/></marker>'
            for mid, col in self.markers.items())
        head = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.w} {self.h}" width="{self.w}" '
                f'height="{self.h}" font-family="{FONT}" role="img" aria-labelledby="t d">\n'
                f'<title id="t">{esc(self.title)}</title>\n<desc id="d">{esc(self.desc)}</desc>\n'
                f'<defs>{defs}</defs>\n'
                f'<rect x="0.75" y="0.75" width="{self.w - 1.5}" height="{self.h - 1.5}" rx="16" fill="#ffffff" '
                f'stroke="#e5e7eb" stroke-width="1.5"/>\n')
        with open(path, 'w') as fh:
            fh.write(head + '\n'.join(self.items) + '\n</svg>\n')
