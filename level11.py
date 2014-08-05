'''
11
The given graph was composed by several small graphs which can be extracted in an odd-even way
'''
from PIL import Image, ImageDraw
img = Image.open('cave.jpg')
pix = img.load()
# print size(pix)
# print [x for v in pix for x in v]
# print pix[0, 0]
x, y = img.size
imgs = [Image.new('RGB', (x/2, y/2)) for i in xrange(4)]
pixs = [i.load() for i in imgs]
print img.size, imgs[0].size
for i in xrange(x-1):
    for j in xrange(y-1):
        if not (i % 2 == 0 or j % 2 == 0):
            pixs[0][i/2,j/2] = (pix[i,j][0] / 2, pix[i,j][1] / 2, pix[i,j][2] / 2)

imgs[0].show()
