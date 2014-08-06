'''
2
'''
f = open('cont.txt', 'r')

for line in f:
    for c in line.rstrip():
        if 'a' <= c <= 'z':
            print c
