'''
http://www.pythonchallenge.com
#3 url=http://www.pythonchallenge.com/pc/def/equality.html

'''
import re
def case3(s):
    r = re.compile(r'[a-z]{1}[A-Z]{3}[a-z]{1}[A-Z]{3}[a-z]{1}')
    rlist = r.findall(s)
    newString = ''
    for i in rlist:
        newString = newString+i[4]
    return newString

if __name__=='__main__':
    with open('mess1') as f:
        s=f.read()
    print(case3(s))

#'linkedlist'
