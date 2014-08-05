'''
8
'''
import bz2

# s = 'heai'
# s_c = bz2.compress(s)
# print repr(s_c)
# s_dec = bz2.decompress(s_c)
# print s_dec
un = 'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
pw = 'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'

un_dec = bz2.decompress(un)
pw_dec = bz2.decompress(pw)

print un_dec
print pw_dec
