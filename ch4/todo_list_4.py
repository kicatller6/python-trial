#4.1
#guess_me = 7
#start = 1
#while start <= 7:

#    if guess_me < start:
#        print("Oops")
#        break
#    elif guess_me > start:
#        print("too low")
#    else:
#        print("found it")
#    start+=1

#4.3        
#for x in range(10):
#    print(x)
#4.4
#num_list = [x for x in range(10) if x-1 %2 ]
#print(num_list)
#4.5
#squares = {n:n*n for n in range(10) }
#print(squares)
#4.6
#odd = {x for x in range(10) if x % 2}
#print(odd)
#4.7
#for obj in ('Got :%s' % num for num in range(10)):
#    print(obj)
#4.8
#def good():
#    return ['Harry','Ron','Hermione']
#print(good())    
#4.9
#def get_odds():
#    for x in range(10):
#        if x %2:
#            yield x
#count =0
#for obj in get_odds():
#    count+=1
#    if count == 3:
#        print(obj)
#4.10
#def test(func):
#    def new_function(*args,**kwargs):
#        print('start')
#        result = func(*args,**kwargs)
#        print(result)
#        print('end')
#        return result        
#    return new_function    
#@test
#def add_num(a,b):
#    return a+b
#add_num(35,5)
#4.11
#class OopsException(Exception):
#    pass
#oop=[1,2,3]
#try:
#    oop[5]
#except IndexError as e:
#    print('caugth an Oops')
#    raise OopsException(e)
#4.12
#title = ['Creature of Habit','Crewel Fate']
#plots = ['A nun turns into a monster','A Hunted yarn shop']
#movies =dict(zip(title,plots)) 
#print(movies)