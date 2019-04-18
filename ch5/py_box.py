import sys
print('programing argument:',sys.argv)

from module.report import get_description as rep

description = rep()
print("Today's weather",description)

""" from module  import daily,weekly

print("Daily forecast:",daily.forecast())
print("weekly forecast:")
for number,outlook in enumerate(weekly.forecast(),1):
    print(number,outlook)

periodic_table = {'Hydrogen':1,'Helium':2}
carbon = periodic_table.setdefault('Carbon',12)
print(carbon)
print(periodic_table)


from collections import defaultdict
periodic_table = defaultdict(bool)
periodic_table['Hydrogen'] = 1
periodic_table['Lead']
print(periodic_table)

def no_idea():
    return 'Huh?'
bestiary = defaultdict(no_idea)
bestiary = defaultdict(lambda:'Huh?')       #等價上一行
bestiary['A'] = 'Abominable Snowman'
bestiary['B'] = 'Basilisk'
print (bestiary['A'],bestiary['B'],bestiary['C'])

food_counter = defaultdict(int)
for food in ['spam','spam','eggs','spam']:
    food_counter[food] += 1
for food,count in food_counter.items():
    print(food,count)

#Counter:
from collections import Counter
breakfast = ['spam','spam','eggs','spam']
breakfast_counter = Counter(breakfast)      #collections.Counter物件
print(breakfast_counter)                    
print((breakfast_counter.most_common()))      #list物件

lunch = ['eggs','eggs','bacon']
lunch_counter = Counter(lunch)
print(breakfast_counter | lunch_counter)

#OrderedDict::
quote = {'Moe':'A wise guy ,huh?','Larry':'Ow!','Curly':'Nyuk nyuk!'}
for stooge in quote:
    print(stooge)
from collections import OrderedDict
quote = OrderedDict({'Moe':'A wise guy ,huh?','Larry':'Ow!','Curly':'Nyuk nyuk!'})
for stooge in quote:
    print(stooge)
#deque:
from collections import deque
def palindrome(word):               #回文檢查器
    dq = deque(word)
    while len(dq)>1:
        if dq.popleft() != dq.pop():
            return False
    return True
print(palindrome('a#'))
def another_palinfrome(word):       #快速寫法
    return word ==word[::-1]

#itertoos::
import itertools
for item in itertools.chain([1,2],['a','b']):       #丟入不同型態的引數 轉換為可迭代的單一項目
    print(item)

count = 0
for item in itertools.cycle([1,2]):                 #無限循環迭代內容引數
    print(item)
    count +=1
    if count ==10 : break

def mutiple(a,b):
    return a*b
for item in itertools.accumulate([1,2,3,4],mutiple):        #累進迭代器(預設為加法)
    print(item)

#pprint:
from collections import OrderedDict
from pprint import pprint
quote = ['Hey','What\'s going on today','Today',':I\'m not very comfortable today']
pprint(quote)

 """