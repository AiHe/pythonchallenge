import gzip
import urllib
import os.path
import difflib

file_name = './deltas.gz'


def download():
    f = urllib.urlopen('http://www.pythonchallenge.com/pc/return/deltas.gz')
    w = open(file_name, 'w')
    w.write(f.read())
    w.close()

if not os.path.isfile(file_name):
    download()
f = gzip.open(file_name, 'rb')
file_content = f.readlines()
f.close()

# print file_content
p1 = open('p1.png', 'w')
p2 = open('p2.png', 'w')

list_1 = []
list_2 = []
i = 0

# import binascii

# ff = open("cat.txt", "r")
# txt = ff.read()
# ff.close()

# Split on space, join back with no separator
# txt = "".join(txt.split())


for line in file_content:
    # print line
    # i += 1
    # if i > 2:
    #     break
    sps = line.rstrip().split('   ')
    # print sps[0]
    # print sps[1]
    list_1.append(sps[0])
    list_2.append(sps[1])

# print ''.join((''.join(list_1)).split())
# image_1 = binascii.unhexlify(''.join((''.join(list_1)).split()))
# image_2 = binascii.unhexlify(''.join((''.join(list_2)).split()))

# print image_1
# print image_2
# print type(image_1)

# p1.write(image_1)
# p2.write(image_2)

out = ['', '', '']
diff = list(difflib.ndiff(list_1, list_2))
print diff

for line in diff:
    string = [chr(int(c, 16)) for c in line[2:].split()]
    if line[0] == '-':
        out[0] += ''.join(string)
    elif line[0] == '+':
        out[1] += ''.join(string)
    else:
        out[2] += ''.join(string)

for i in range(3):
    open('18_%d.png' % i, 'wb').write(out[i])

p1.close()
p2.close()
