'''
http://www.pythonchallenge.com
'''
#1 url = http://www.pythonchallenge.com/pc/def/map.html
ciphertext = \
'''
g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. \
bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle.\
 sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. 
'''
offset = 2
def case1(ciphertext, offset):
    import string
    '''
    K-M O-Q E-G
    input ciphertext and offset
    ord and chr
    A to Z means 65 to 90
    a to z, from 97 to 122
    :return: plain text
    '''
    # it should be 0 < offset < 26
    if offset > 25 or offset < -25:
        raise ValueError('Please set reasonable offset between -25 to 25')
    if offset < 0:
        offset = offset + 26
    letters = string.ascii_letters
    lcletters = string.ascii_lowercase
    luletters = string.ascii_uppercase
    def conv(char, offset):
        if char not in letters: # if not letters, return it the same
            return char
        neword = ord(char) + offset
        # we have only positive offset now and lower than 26
        if (char in luletters and neword > 90) or (char in lcletters and neword > 122):
            neword = neword -26
        newchar = chr(neword)
        return newchar
    plain_text = ''
    for i in ciphertext:
        plain_text = plain_text + conv(i, offset)
    return plain_text

print(case1(ciphertext, offset))
'''
i hope you didnt translate it by hand. thats what computers are for. 
doing it in by hand is inefficient and that's why this text is so long.
using string.maketrans() is recommended. now apply on the url.
'''
'''
>>> string1 = 'http://www.pythonchallenge.com/pc/def/map.html'
>>> print(case1(string1,2))
jvvr://yyy.ravjqpejcnngpig.eqo/re/fgh/ocr.jvon
'''
# it's not a valid url, but just try to replace the 'map' to 'ocr'

'''
try another way:
intab = 'aeiou'
outtab = '12345'
s = 'this is string example....wow!!!'
print(s.translate({ord(x): y for (x, y) in zip(intab, outtab)}))
'''
