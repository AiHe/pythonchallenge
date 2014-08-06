'''
5
'''
import pickle
import urllib
# favorite_color = { "lion": "yellow", "kitty": "red" }
#
# pickle.dump( favorite_color, open( "save.p", "wb" ) )
#
# favorite_color_new = pickle.load( open( "save.p", "rb" ) )
#
# print favorite_color_new

# def getContent(url):
#     f = urllib.urlopen(url)
#     return f.read()

url = 'http://www.pythonchallenge.com/pc/def/banner.p'

obj = pickle.load(urllib.urlopen(url))
print obj
for ele in obj:
    print ''.join(e[0]*e[1] for e in ele)
