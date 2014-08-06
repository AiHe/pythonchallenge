'''
7
'''
from PIL import Image
import urllib, cStringIO
im = Image.open(cStringIO.StringIO(urllib.urlopen('http://www.pythonchallenge.com/pc/def/oxygen.png').read()), 'r')
print im.info
print im.size
x, y = im.size
y = y / 2
prev = None
for i in xrange(x):
    cur = chr(im.getpixel((i, y))[0])
    if prev is not cur:
        prev = cur
        print cur,
print
l = [105,10,16,101,103,14,105,16,121]
for i in l:
    if i < 100:
        i += 100
    print chr(i)
