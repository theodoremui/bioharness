"""Assemble proposal sources into standalone Markdown files.

Directives in sources:
  @include name            inline src/parts/name.md
  @fig label | path | text figure with caption; refer to it as {fig:label}
  ## Title {#label}        numbered heading; refer to it as {sec:label}
  ## Title {-}             unnumbered heading
  ## Appendix: Title {#l}  appendix heading (A, B, ...)
  [@key] / [@a; @b]        parenthetical citation;  @{key} narrative citation
"""
import re, sys, os
from bib import BIB

SRC = os.path.join(os.path.dirname(__file__), 'src')
OUTDIR = sys.argv[1]
names = sys.argv[2:]


def expand(text, depth=0):
    out = []
    for line in text.split('\n'):
        m = re.match(r'^@include\s+(\S+)\s*$', line)
        if m:
            out.append(expand(open(os.path.join(SRC, 'parts', m.group(1) + '.md')).read().rstrip('\n'), depth + 1))
        else:
            out.append(line)
    return '\n'.join(out)


def build(name):
    text = expand(open(os.path.join(SRC, name + '.md')).read())
    lines = text.split('\n')
    sec, sub, app = 0, 0, 0
    labels, figs = {}, {}
    out = []
    # pass 1: headings and figures
    nfig = 0
    for line in lines:
        h = re.match(r'^(#{2,3}) (.*?)\s*(\{(#[\w-]+|-)\})?\s*$', line)
        f = re.match(r'^@fig\s+([\w-]+)\s*\|\s*([^|]+?)\s*\|\s*(.+)$', line)
        if h and not line.startswith('####'):
            level, title, tag = len(h.group(1)), h.group(2), h.group(4)
            if title.startswith('Appendix:'):
                app += 1
                letter = chr(64 + app)
                title = f'Appendix {letter}. {title[9:].strip()}'
                if tag and tag != '-':
                    labels[tag[1:]] = f'Appendix {letter}'
                out.append(f'## {title}')
                sec_mode = 'app'
                continue
            if tag == '-' or level == 2 and title in ('Abstract', 'References'):
                out.append(f'{h.group(1)} {title}')
                continue
            if level == 2:
                sec += 1; sub = 0
                num = f'{sec}'
                out.append(f'## {num}. {title}')
            else:
                sub += 1
                num = f'{sec}.{sub}'
                out.append(f'### {num} {title}')
            if tag:
                labels[tag[1:]] = f'Section {num}'
            continue
        if f:
            nfig += 1
            lab, path, cap = f.groups()
            figs[lab] = nfig
            alt = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', cap)
            alt = re.sub(r'\[@[^\]]*\]|@\{[\w-]+\}', '', alt)
            alt = re.sub(r'[*_`]', '', alt).split('. ')[0].strip().rstrip('.')
            out.append(f'![{alt}]({path})')
            out.append('')
            out.append(f'**Figure {nfig}.** {cap}')
            continue
        out.append(line)
    body = '\n'.join(out)

    def ref(m):
        kind, lab = m.group(1), m.group(2)
        if kind == 'fig':
            if lab not in figs:
                raise SystemExit(f'{name}: unknown figure {lab}')
            return f'Figure {figs[lab]}'
        if lab not in labels:
            raise SystemExit(f'{name}: unknown section {lab}')
        return labels[lab]
    body = re.sub(r'\{(fig|sec):([\w-]+)\}', ref, body)

    used = []

    def use(k):
        if k not in BIB:
            raise SystemExit(f'{name}: unknown citation {k}')
        if k not in used:
            used.append(k)
        return BIB[k]

    def paren(m):
        keys = [k.strip().lstrip('@') for k in m.group(1).split(';')]
        return '(' + '; '.join(f'[{use(k)[0]}]({use(k)[2]})' for k in keys) + ')'
    body = re.sub(r'\[(@[\w-]+(?:\s*;\s*@[\w-]+)*)\]', paren, body)

    def narr(m):
        k = m.group(1)
        short = use(k)[0]
        a, y = short.rsplit(', ', 1)
        return f'[{a} ({y})]({use(k)[2]})'
    body = re.sub(r'@\{([\w-]+)\}', narr, body)
    # reference list
    if '@references' in body:
        refs = sorted(used, key=lambda k: BIB[k][1].lower())
        lst = '\n'.join(f'- {BIB[k][1]} {BIB[k][2]}' for k in refs)
        body = body.replace('@references', lst)
    body = re.sub(r'([^\n])\n(#{1,3} )', r'\1\n\n\2', body)
    body = re.sub(r'\n{3,}', '\n\n', body).strip() + '\n'
    for leftover in re.findall(r'^@\w+.*$', body, re.M):
        raise SystemExit(f'{name}: unprocessed directive {leftover}')
    return body


for n in names:
    md = build(n)
    path = os.path.join(OUTDIR, n + '.md')
    open(path, 'w').write(md)
    words = len(re.sub(r'!\[[^\]]*\]\([^)]*\)|\([^)]*https?://[^)]*\)', '', md).split())
    print(f'{n}: {words} words, {md.count("**Figure ")} figures')
