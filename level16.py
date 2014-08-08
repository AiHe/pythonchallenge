'''
16
'''
from PIL import Image

img = Image.open('mozart.gif')
tar = 195
i = 0
ll = list(img.getdata())
for l in [list(t) for t in zip(*[iter(ll)]*img.size[0])]:
    pos = l.index(tar)
    l = l[pos:] + l[0:pos]
    img2 = Image.new(img.mode, (img.size[0], 1))
    img2.putdata(l)
    img.paste(img2, (0, i, img.size[0], i+1))
    i += 1

img.show()

# Image.fromstring()
