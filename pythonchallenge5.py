'''
http://www.pythonchallenge.com
#4 url=http://www.pythonchallenge.com/pc/def/peak.html
peak hell sounds like pickle, goto the web address: "http://www.pythonchallenge.com/pc/def/pickle.html", we got yes.
in the url peak.html, we found <peakhell src="banner.p"/>, go to the web address, we got a pickle file:
http://www.pythonchallenge.com/pc/def/banner.p
it seems like an image described by a 2 dimensions list with " " and "#", as below:
[(' ', 95)]
[(' ', 14), ('#', 5), (' ', 70), ('#', 5), (' ', 1)]
[(' ', 15), ('#', 4), (' ', 71), ('#', 4), (' ', 1)]
[(' ', 15), ('#', 4), (' ', 71), ('#', 4), (' ', 1)]
...
print this list each line, the result is "channel"
'''

from urllib import request
import pickle
url = "http://www.pythonchallenge.com/pc/def/banner.p"
with request.urlopen(url) as f:
    data = pickle.loads(f.read())
line=''
print('BEGIN:')
for items in data:
    for i in items:
        a,b = i
        line = line + a*b
    print(line)
    line = ''
print('END!')

