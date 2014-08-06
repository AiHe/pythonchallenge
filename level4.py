'''
4
'''
import urllib
import re
def getContent(url):
    f = urllib.urlopen(url)
    content = f.read()
    print content
    return content
def next(id):
    url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' + str(id)
    data = getContent(url)
    if 'and the next nothing is' in data:
        return re.findall('\d+', data)[-1]
    elif "Yes. Divide by two and keep going." in data:
        return str(int(id)/2)
    else:
        return None

i = 0
id = 12345
while i < 400 and id is not None:
    id = next(id)
    print id
    i += 1
