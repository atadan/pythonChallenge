'''
http://www.pythonchallenge.com
#11 url="http://www.pythonchallenge.com/pc/return/evil.html"
title = dealing evil
'''

'''
http://www.pythonchallenge.com/pc/return/evil1.jpg
http://www.pythonchallenge.com/pc/return/evil2.jpg - not jpg - .gfx
http://www.pythonchallenge.com/pc/return/evil2.gfx is a file
http://www.pythonchallenge.com/pc/return/evil3.jpg - no more evels
http://www.pythonchallenge.com/pc/return/evil4.jpg - error
http://www.pythonchallenge.com/pc/return/evil5.jpg - 404
curl -u huge:file http://www.pythonchallenge.com/pc/return/evil4.jpg 
Bert is evil! go back!

it looks like there are something in "http://www.pythonchallenge.com/pc/return/evil2.gfx"
'''

filename = './test/evil2.gfx'
with open(filename,'rb') as f:
    data = f.read()

#将原数据分成5份，第一份从0开始，间隔5个位置取数，第二份从1开始，间隔5个位置取数……
for i in range(5):
    open('./test/%d.jpg'%i,'wb').write(data[i::5])

#生成5个图片，分别显示：
# dis pro port ional (no ity)
# http://www.pythonchallenge.com/pc/return/disproportional.html
