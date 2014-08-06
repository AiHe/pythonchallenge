'''
1
'''
f = open('cont.txt', 'r')
line = ''
for l in f:
    line += l.rstrip()

res = ''
for c in line:
    if not c == ' ' and not c == '.' and not c == '(' and not c == ')' and not c == '\'':
        res += chr((ord(c)-ord('a')+2) % 26 + ord('a'))
    else:
        res += c
print res
