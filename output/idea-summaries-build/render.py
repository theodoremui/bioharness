"""Render SVG files to PNG with headless Chrome so figures can be inspected.

Usage: python3 -B output/idea-summaries-build/render.py OUTDIR [--scale 2] file1.svg file2.svg ...
"""
import os, re, subprocess, sys, tempfile

CH = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"


def main(argv):
    outdir = argv[1]
    scale = 2
    files = argv[2:]
    if files and files[0] == '--scale':
        scale, files = float(files[1]), files[2:]
    os.makedirs(outdir, exist_ok=True)
    for s in files:
        head = open(s).read(800)
        w = int(float(re.search(r'width="([\d.]+)"', head).group(1)))
        h = int(float(re.search(r'height="([\d.]+)"', head).group(1)))
        out = os.path.join(outdir, os.path.basename(s).replace('.svg', '.png'))
        for _ in range(3):
            try:
                with tempfile.TemporaryDirectory() as ud:
                    subprocess.run([CH, '--headless=new', '--disable-gpu', '--hide-scrollbars',
                                    f'--force-device-scale-factor={scale}', f'--user-data-dir={ud}',
                                    f'--window-size={w},{h}', f'--screenshot={out}', 'file://' + os.path.abspath(s)],
                                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=60)
                break
            except subprocess.TimeoutExpired:
                continue
        print(out)


if __name__ == '__main__':
    main(sys.argv)
