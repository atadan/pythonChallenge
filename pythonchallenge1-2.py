'''
http://www.pythonchallenge.com
#1-2 url = http://www.pythonchallenge.com/pc/def/map.html
to build a Caesar cipher system as the roles described as the wiki said:
https://en.wikipedia.org/wiki/Caesar_cipher
letters only no matter lower case or upper case, return none letter directly
tools: ord chr and str.maketrans() and str.translate()
    A to Z, means 65 to 90
    a to z, means 97 to 122
'''
shiftValue = -2
plaintext = \
'''
i hope you didnt translate it by hand. thats what computers are for. 
doing it in by hand is inefficient and that's why this text is so long.
using string.maketrans() is recommended. now apply on the url.
'''
ciphertext = \
'''
g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. \
bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle.\
 sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. 
'''
def shiftValueConvert(shiftValue):
    '''
    convert caesar cipher shift value from any possible value to a positive int number between 0-25
    :param shiftValue: int nubmer
    :return: the int number between 0-25
    '''
    if type(shiftValue) == type(1):
        return shiftValue%26
    else:
        raise ValueError('please input int number only!')

def Caesar_cipher(text, shiftValue, encryptOrDecrypt):
    import string
    lc = string.ascii_lowercase
    lu = string.ascii_uppercase
    if encryptOrDecrypt == 'encrypt':
        shiftValue = shiftValueConvert(shiftValue)
    else:
        shiftValue = shiftValueConvert(-shiftValue)

    lcShift = lc[shiftValue:] + lc[:shiftValue]
    luShift = lu[shiftValue:] + lu[:shiftValue]
    convMap = str.maketrans(lc+lu,lcShift+luShift)
    print(convMap)
    return text.translate(convMap)

def Caesar_cipher_encrypt(plaintext, shiftValue):
    return Caesar_cipher(plaintext, shiftValue, 'encrypt')

def Caesar_cipher_decrypt(ciphertext, shiftValue):
    return Caesar_cipher(ciphertext, shiftValue, 'decrypt')

#test
if __name__ == '__main__':
    test1 = Caesar_cipher_encrypt(plaintext, shiftValue)
    test2 = Caesar_cipher_decrypt(ciphertext, shiftValue)
    print('this is test1:\n')
    print(test1)
    print('this is test2:\n')
    print(test2)

