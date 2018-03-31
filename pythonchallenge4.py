'''
http://www.pythonchallenge.com
#4 url=http://www.pythonchallenge.com/pc/def/linkedlist.html
http://www.pythonchallenge.com/pc/def/linkedlist.php
follow the chain
urllib may help. DON'T TRY ALL NOTHINGS, since it will never end. 400 times is more than enough.

'''
from urllib import request
import re

baseurl = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
nn = '12345' #start nn = '12345'
i = 1
r=re.compile(r'[0-9]\d*')
while i <= 400:
    with request.urlopen(baseurl+nn) as f:
        data = f.read()
        ss = data.decode('utf-8')
        print("it's the %s times HTTP request."%i)
        print('ss is :',ss)
        nothinglist = r.findall(ss)
        if len(nothinglist) <1:
            if ss=='Yes. Divide by two and keep going.':
                nn = str(int(nn)/2)
            else:
                raise(ValueError(ss))
        else:
            nn = nothinglist[-1]
        i=i+1
#'peak.html'
