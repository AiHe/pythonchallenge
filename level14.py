'''
14
'''

# res = 0
# for i in xrange(100):
#     res += 2*i + 1
# print res

ll = [[i, i - 1, i - 1, i - 2] for i in xrange(100, 1, -2)]
l = [i for ii in ll for i in ii]
direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]

from PIL import Image
img = Image.open('wire.png')
pix = img.load()

img_new = Image.new('RGB', (100, 100))
pix_new = img_new.load()

pos = (-1, 0)
v = 0
idx = 0
for t in l:
    for i in xrange(t):
        pos = tuple(map(sum, zip(pos, direction[v])))
        # print pos, (l[idx], 0)
        pix_new[pos] = pix[(idx, 0)]
        idx += 1
    v = (v+1) % 4

img_new.show()
