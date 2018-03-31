'''
http://www.pythonchallenge.com
#8 url="http://www.pythonchallenge.com/pc/def/integrity.html"
'''

from bs4 import BeautifulSoup
from urllib import request

url = "http://www.pythonchallenge.com/pc/def/integrity.html"
with request.urlopen(url) as f:
    html = f.read()
soup = BeautifulSoup(html, "lxml")
'''
comment = soup.findAll(text=lambda text:isinstance(text,Comment))
'''

username = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
password = b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'
import bz2
print(bz2.decompress(username))
print(bz2.decompress(password))

'''
b'huge'
b'file'
'''
