'''
13
faultCode and faultString indicate we should use xmlprclib
According to https://docs.python.org/2/library/xmlrpclib.html
'''
import xmlrpclib

proxy = xmlrpclib.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")

print proxy.system.listMethods()
print proxy.system.methodSignature('phone')
print proxy.system.methodHelp('phone')
print proxy.phone('Bert')
