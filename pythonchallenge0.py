'''
http://www.pythonchallenge.com
'''

def case0():
    url = 'http://www.pythonchallenge.com/pc/def/0.html'
    i = str(2**38)
    newurl = url.replace('0',i)
    return newurl
