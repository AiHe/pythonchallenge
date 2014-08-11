import requests
import urllib
import re


def get_content(url):
    # f = urllib.urlopen(url)
    # data = f.read()
    f = requests.get(url)
    data = f.text
    cookie = f.cookies['info']
    print data, cookie
    return data, cookie

list_cookies = []
# url = 'http://www.pythonchallenge.com/pc/return/romance.html'

id = 12345
url_ = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing='
i = 0
while i < 0 and id:
    url_1 = url_ + str(id)
    data, cookie = get_content(url_1)
    id = re.findall('\d{2,}', data)
    if id:
        id = id[0]
        list_cookies.append(cookie)
    else:
        break
    i += 1

url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php'
r = requests.get(url)
print r.cookies.keys()
print r.cookies['info']
list_cookies.append(r.cookies['info'])
#
# print ''.join(list_cookies)

import bz2

s = 'BZh91AY%26SY%94%3A%E2I%00%00%21%19%80P%81%11%00%AFg%9E%A0+%00hE%3DM%B5%23%D0%D4%D1%E2%8D%06%A9%FA%26S%D4%D3%21%A1%EAi7h%9B%9A%2B%BF%60%22%C5WX%E1%ADL%80%E8V%3C%C6%A8%DBH%2632%18%A8x%01%08%21%8DS%0B%C8%AF%96KO%CA2%B0%F1%BD%1Du%A0%86%05%92s%B0%92%C4Bc%F1w%24S%85%09%09C%AE%24%90'

print repr(urllib.unquote(s))
print repr(urllib.unquote_plus(s))
s_dec = bz2.BZ2Decompressor().decompress(urllib.unquote_plus(s))
print s_dec

import xmlrpclib

proxy = xmlrpclib.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")

print proxy.system.listMethods()
print proxy.system.methodSignature('phone')
print proxy.system.methodHelp('phone')
print proxy.phone('Leopold')


url = 'http://www.pythonchallenge.com/pc/stuff/violin.php'
cookies = dict(info='the flowers are on their way')
f = requests.get(url, cookies=cookies)
data = f.text
cookies_new = f.cookies
print data
print cookies_new.keys()
