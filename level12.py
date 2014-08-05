'''
12
sample the gfx file with step length 5
'''
f = open('evil2.gfx')
s = f.read()
# print repr(s)

pix = [s[i::5] for i in xrange(5)]

for i in xrange(5):
    f = open('evil' + str(i) + '.jpg', 'w')
    f.write(pix[i])
    f.close()
