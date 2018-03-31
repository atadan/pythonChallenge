'''
http://www.pythonchallenge.com
#2 url = http://www.pythonchallenge.com/pc/def/ocr.html
find rare characters

collections.defaultdict

sort dict by values:
import operator
x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
sorted_x = sorted(x.items(), key=operator.itemgetter(1))

sort dict by keys:
import operator
x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
sorted_x = sorted(x.items(), key=operator.itemgetter(0))
'''

def rarecharacter(s):
    import operator, collections
    lists = collections.defaultdict(int)
    for k in s:
        lists[k]+=1

    sorted_lists = sorted(lists.items(), key=operator.itemgetter(1))

    return sorted_lists

if __name__=='__main__':
    with open('mess') as f:
        s=f.read()

    print(rarecharacter(s))

#'equality'
