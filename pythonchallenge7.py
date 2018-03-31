'''
http://www.pythonchallenge.com
#6 url="http://www.pythonchallenge.com/pc/def/oxygen.html"
the oxygen.html has nothing comment but an "oxygen.png" image
imgurl = "http://www.pythonchallenge.com/pc/def/oxygen.png"
the image has a gray strip in the middle
got the pixel of the img by PIL, in python3, pip install pillow to get PIL
convert image to numpy array, got all the RGBA data, the feature of gray color is R=G=B
put RGB value of the middle gray line into a list, get one of each the same 7 numbers
convert the list to char, we got:
"smart guy, you made it. the next level is [105, 110, 116, 101, 103, 114, 105, 116, 121]"
convert the new list to the result:
"integrity"
'''
from PIL import Image
from urllib import request
import numpy
import re
import io

imgurl = "http://www.pythonchallenge.com/pc/def/oxygen.png"
r = re.compile(r'\d+')
with request.urlopen(imgurl) as f:
    imgfile = f.read()
img = Image.open(io.BytesIO(imgfile))
pix = numpy.array(img)
row=pix[pix.shape[0]//2,:,0]
nrow = row[::7]
result = ""
result1=""
for i in nrow:
    result = result + chr(i)
print(result)
nlist = r.findall(result)
for i in nlist:
    result1 = result1+chr(int(i))
print(result1)

