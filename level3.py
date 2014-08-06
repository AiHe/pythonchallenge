'''
3
'''
import re
f = open('cont.txt', 'r')
for line in f:
    p = re.compile('[^A-Z]+[A-Z]{3}[a-z][A-Z]{3}[^A-Z]+')
    m = p.search(line.rstrip())
    if m:
        print m.group()
