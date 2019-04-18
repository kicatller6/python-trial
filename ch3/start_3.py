#tuple:一旦行程就再也不能改變
#list:可以自由增刪
#pop()使用的順序代表FIFO和FILO的關係
# &(inintersection)...|(Union)...-(difference)...
#互斥或: ^(symmetric_different)
#子集:<= (issubset)...真子集: < (必須兩集合不相等)
#超集合: >= (issuperset)...真超集合: >(兩集合不相等)
life =dict()
cats = ['Henri','Grumpy','Lucy']
plants = dict()
other = dict()
octopi = dict()
emus = dict()
life.update({'animals':{'cats':cats,'octopi':octopi,'emus':emus},'plants':plants,'other':other})
print(life.keys())
print(life['animals']['cats'])