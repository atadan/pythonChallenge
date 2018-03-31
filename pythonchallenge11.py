'''
http://www.pythonchallenge.com
#11 url="http://www.pythonchallenge.com/pc/return/5808.html"
title = odd even
'''

from PIL import Image
from urllib import request
import numpy
import re
import io

password_mgr = request.HTTPPasswordMgrWithDefaultRealm()
username = 'huge'
password = 'file'
imgurl = "http://www.pythonchallenge.com/pc/return/cave.jpg"
password_mgr.add_password(None, imgurl, username, password)
handler = request.HTTPBasicAuthHandler(password_mgr)
opener = request.build_opener(handler)
request.install_opener(opener)
with request.urlopen(imgurl) as f:
    imgfile = f.read()
img = Image.open(io.BytesIO(imgfile))
pix = numpy.array(img)
print(pix)
