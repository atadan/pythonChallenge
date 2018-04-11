'''
http://www.pythonchallenge.com
#11 url="http://www.pythonchallenge.com/pc/return/5808.html"
title = odd even
'''

'''
直接从网络抓取图片到本地再处理的代码暂时注释，在调试过程中使用本地图片
from urllib import request
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
'''

'''
下面的算法希望利用numpy来完成图像数据的处理，
但是在Image.fromarray这个函数转化过程中，似乎出现了问题，
导致转化后的图像信息丢失了原有的RGB信息，无法得出有意义的结果，
经过1周左右的尝试，暂时放弃，转而利用直接处理Image对象的方法
（参考https://the-python-challenge-solutions.hackingnote.com/level-11.html）
filename = "./test/cave.jpg"
img = Image.open(filename)
pix = np.array(img)
high,wide, rgb = pix.shape
oddpix = np.zeros((int(high//2),int(wide//2),rgb))
evenpix = np.zeros((int(high//2),int(wide//2),rgb))
for i in range(high):
    for j in range(wide):
        if (i+j)%2 == 0:
            oddpix[int(i//2),int(j//2)]=pix[i,j]
            print(oddpix[int(i//2),int(j//2)], pix[i,j])
        else:
            evenpix[i//2,j//2]=pix[i,j]
odd=Image.fromarray(oddpix,'RGB')
even = Image.fromarray(evenpix,'RGB')
odd.save('./test/odd.jpg')
even.save('./test/even.jpg')
'''
from PIL import Image

filename = "./test/cave.jpg"
im = Image.open(filename)
(w, h) = im.size

even = Image.new('RGB', (w // 2, h // 2))
odd = Image.new('RGB', (w // 2, h // 2))

for i in range(w):
    for j in range(h):
        p = im.getpixel((i,j))
        if (i+j)%2 == 1:
            odd.putpixel((i // 2, j // 2), p)
        else:
            even.putpixel((i // 2, j // 2), p)
even.save('./test/even.jpg')
odd.save('./test/odd.jpg')

# got evil
