import sys
from PIL import Image, ImageDraw
out, W = sys.argv[1], int(sys.argv[2]); files = sys.argv[3:]
ims = []
for f in files:
    im = Image.open(f).convert('RGB'); r = W / im.width; ims.append((f.split('/')[-1], im.resize((W, int(im.height * r)))))
H = sum(i.height + 26 for _, i in ims)
s = Image.new('RGB', (W, H), (200, 200, 200)); d = ImageDraw.Draw(s); y = 0
for n, i in ims:
    d.text((6, y + 6), n, fill='black'); s.paste(i, (0, y + 24)); y += i.height + 26
s.save(out); print(s.size)
