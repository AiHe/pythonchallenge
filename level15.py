'''
15
'''

from datetime import date

ds = []
for year in xrange(1006, 1997, 10):
    if year % 4 == 0:
        d = date(year, 1, 27)
        if d.weekday() == 1:
            ds.append(d)

print ds[-2]
