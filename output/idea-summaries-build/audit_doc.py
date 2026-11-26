"""Audit a proposal markdown file against the drafting guide.

Usage: python3 -B output/idea-summaries-build/audit_doc.py docs/research-plans/05-*.md [...]

Checks: em-dashes and en-dashes, ' -- ', \\operatorname, banned words, image links that do
not resolve, citation links [n](#ref-n) without a matching anchor, anchors never cited,
prose word count (excluding the References section and code blocks), runs of three or more
very short sentences (staccato), and frequent antithesis patterns.
"""
import os
import re
import sys

BANNED = ['delve', 'tapestry', 'landscape', 'underscore', 'pivotal', 'seamless', 'crucially',
          'actually', 'exactly', 'truly', 'game-changer', 'paradigm shift', 'unlock the',
          'it is worth noting', 'in conclusion', 'furthermore,', 'moreover,']
ANTITHESIS = [r"\bis not (?:just |merely |simply )?[^.;]{1,60}[;,] (?:it|this|they) (?:is|are)\b",
              r"\bisn't [^.;]{1,60}[;,] it's\b", r"\bnot because [^.;]{1,60}, but because\b",
              r"\bnot [^.;]{1,40}, but [^.;]{1,40}\b"]


def audit(path):
    src = open(path, encoding='utf-8').read()
    base = os.path.dirname(path)
    out = []
    for ch, name in [('—', 'em-dash'), ('–', 'en-dash')]:
        n = src.count(ch)
        if n:
            lines = [i + 1 for i, l in enumerate(src.splitlines()) if ch in l][:8]
            out.append(f'{name}: {n} (lines {lines})')
    if ' -- ' in src:
        out.append('double-hyphen dash " -- " present')
    if '\\operatorname' in src:
        out.append('\\operatorname present')
    body = src.split('\n## References')[0]
    prose = re.sub(r'```.*?```', ' ', body, flags=re.S)
    low = prose.lower()
    for w in BANNED:
        c = len(re.findall(r'\b' + re.escape(w), low))
        if c:
            out.append(f'banned word "{w}": {c}')
    for pat in ANTITHESIS:
        hits = re.findall(pat, prose, flags=re.I)
        if len(hits) > 1:
            out.append(f'antithesis pattern x{len(hits)}: {hits[:2]}')
    for m in re.finditer(r'!\[[^\]]*\]\(([^)]+)\)', src):
        p = os.path.normpath(os.path.join(base, m.group(1)))
        if not os.path.exists(p):
            out.append(f'missing image: {m.group(1)}')
    cited = set(re.findall(r'\]\(#ref-(\d+)\)', src))
    anchors = set(re.findall(r'<a id="ref-(\d+)"></a>', src))
    if cited - anchors:
        out.append(f'cited without anchor: {sorted(cited - anchors, key=int)}')
    if anchors - cited:
        out.append(f'reference never cited: {sorted(anchors - cited, key=int)}')
    text = re.sub(r'!\[[^\]]*\]\([^)]+\)', ' ', prose)
    text = re.sub(r'\$\$.*?\$\$', ' ', text, flags=re.S)
    words = len(re.findall(r"[A-Za-z][A-Za-z'\-]*", text))
    out.append(f'prose words (excl. references, code, display math): {words}')
    sents = re.split(r'(?<=[.!?])\s+', re.sub(r'\s+', ' ', re.sub(r'[#>*|`]', ' ', text)))
    run, runs = 0, 0
    for s in sents:
        if 0 < len(s.split()) < 8:
            run += 1
            if run == 3:
                runs += 1
        else:
            run = 0
    if runs:
        out.append(f'staccato runs (3+ consecutive sentences under 8 words): {runs}')
    figs = len(re.findall(r'!\[', src))
    out.append(f'figures embedded: {figs}; references: {len(anchors)}')
    print(f'== {path}')
    for o in out:
        print('   ' + o)


if __name__ == '__main__':
    for p in sys.argv[1:]:
        audit(p)
