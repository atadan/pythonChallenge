'''
http://www.pythonchallenge.com
#6 url="http://www.pythonchallenge.com/pc/def/channel.html"
we got the html comment "<!-- <-- zip -->" in the web source code, then goto "http://www.pythonchallenge.com/pc/def/zip.html"
we got "yes. find the zip. ".
I guess it's not about the zip function in python, since there's no data in all the area.
someone tell me that try to this address to get a zip file:"http://www.pythonchallenge.com/pc/def/channel.zip"
then we got lot of file,

in the readme.txt, we know how to start this challenge:
welcome to my zipped list.
hint1: start from 90052
hint2: answer is inside the zip

in the 90052.txt, we got below:
Next nothing is 94191

collect the comment.
collect each files'comment in the zip file, and print the comment, got hockey by letters oxygen
goto "http://www.pythonchallenge.com/pc/def/hockey.html"
it's in the air. look at the letters.
the letters is oxygen
'''
import re
from urllib import request
import zipfile
from io import BytesIO

url = "http://www.pythonchallenge.com/pc/def/channel.zip"
nn = '90052'
p1 = re.compile(r'Next nothing is [0-9]\d*')
p2 = re.compile(r'[0-9]\d*')
localzf = BytesIO()
with request.urlopen(url) as f:
    zf = f.read()
    localzf.write(zf)
    files = zipfile.ZipFile(localzf)
i=0
comments=[]
while i < 1000:
    filename = nn+'.txt'
    s = files.read(filename).decode()
    print(filename,"'s comment:",files.getinfo(filename).comment)
    comments.append(files.getinfo(filename).comment.decode())
    print(str(i),s)
    if p1.match(s):
        nn = p2.search(s).group()
    else:
        print("It's the result: ",s)
        break
    i=i+1
print("".join(comments))
