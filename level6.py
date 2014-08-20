'''
6
'''
import urllib
import re
import zipfile
filename = './channel.zip'


def download():
    f = urllib.urlopen('http://www.pythonchallenge.com/pc/def/channel.zip')
    w = open(filename, 'w')
    w.write(f.read())
    w.close()
# download()
filelist = zipfile.ZipFile(filename)
# print filelist.getinfo('90052.txt').read()
id = '90052'
comments = []
for f in filelist.namelist():
    if id:
        data = filelist.read(str(id) + '.txt')
        comments.append(filelist.getinfo(str(id) + '.txt').comment)
        id = ''.join(re.findall('\d+', data))
        print id

print ''.join(comments)
