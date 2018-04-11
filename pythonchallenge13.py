'''
http://www.pythonchallenge.com
#11 url="http://www.pythonchallenge.com/pc/return/disproportional.html"
title = call him
'''

'''
press number 5, got a link that return xml data:
http://www.pythonchallenge.com/pc/phonebook.php
python xmlrpc
'''

import xmlrpc.client
conn = xmlrpc.client.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
print(conn.system.listMethods())
# ['phone', 'system.listMethods', 'system.methodHelp', 'system.methodSignature', 'system.multicall', 'system.getCapabilities']
print(conn.system.methodHelp("phone"),conn.system.methodSignature("phone"))
# Returns the phone of a person [['string', 'string']]
print(conn.phone("Bert"))
# 555-ITALY
