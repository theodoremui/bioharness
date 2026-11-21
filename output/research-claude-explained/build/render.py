import sys, re, subprocess, os
from PIL import Image
CH = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
outdir = sys.argv[1]; svgs = sys.argv[2:]
pngs = []
for s in svgs:
    head = open(s).read(600)
    w = int(float(re.search(r'width="([\d.]+)"', head).group(1))); h = int(float(re.search(r'height="([\d.]+)"', head).group(1)))
    out = os.path.join(outdir, os.path.basename(s).replace('.svg', '.png'))
    import tempfile
    for attempt in range(3):
        try:
            with tempfile.TemporaryDirectory() as ud:
                subprocess.run([CH, '--headless=new', '--disable-gpu', '--hide-scrollbars', '--force-device-scale-factor=1',
                                f'--user-data-dir={ud}', f'--window-size={w},{h}', f'--screenshot={out}', 'file://' + os.path.abspath(s)],
                               stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=45)
            break
        except subprocess.TimeoutExpired:
            continue
    pngs.append(out)
print('\n'.join(pngs))
