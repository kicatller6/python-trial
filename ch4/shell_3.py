#word = 'letters'
#letters_counts = {letter:word.count(letter) for letter in word}
#print(letters_counts)

#a_set = {number for number in range(1,6) if number %3}
#print (a_set)

#number_thing = (number for number in range(1,6))
#number_list = list(number_thing)
#print(number_list)
#print(list(number_thing))

#def print_kwargs(**args):
#    print('keyword arguments:',args)

#def echo(anything):
#    'echo returns its input arguement'      #doc string
#    return anything
#print(echo.__doc__)


#def sum_arg(*args):
#    return sum(args)

#def run_something(func,*args):
#    return func(*args)
#print(run_something(sum_arg,1,5,6,6,6))

#def outer(saying):
#    def inner():
#        return 'We are the knights who say: "%s"' % saying
#    return inner        #傳回的值是function物件

#a= outer('ni')
#print(a())

#def edit_story(words,func):
#    for word in words:
#        print(func(word))

#def enliven(word):
#    return word.capitalize()+'!'
#stairs = ['thud','meow','thud','hiss']

#edit_story(stairs,lambda wordz :wordz.capitalize()+'!')

#generator:
#def my_range(first = 0,last=10,step=1):
#    number = first
#    while number < last:
#        yield number
#        number += step
#range = my_range(1,5)      
#range_a = (x for x in range(1,5)) #equal to this
#for x in range_a:
#    print(x)
#for x in range:     #perform on one time
#    print(x)    

#decorator:
#def document_it(func):
#    def new_function(*args,**kwargs):
#        print('Running function :',func.__name__)
#        print('Positional arguments:',args)
#        print('Keyword arguments:',kwargs)
#        result = func(*args,**kwargs)
#        print('Result:',result)
#        return result
#    return new_function

#@document_it
#def add_ints(a,b):
#    return a+b

#add_ints(3,5)   #or do the following call
#cooler_add_int = document_it(add_ints)
#cooler_add_int(3,5)

#def square_it(func):
#    def new_function(*args, **kwargs):
#        result = func(*args,**kwargs)
#        return  result* result
#    return new_function

#animal = 'fruitbat'
#def change_and_print_goals():
#    global animal
#    animal = 'pangolin'
#    print('inside',animal)
#change_and_print_goals()

#def change_local():
#    animal = 'wombat'
#    print('local:',locals())
#change_local()
#print(animal)

#short_list = [1,2,3,4]
#position = 5
#try:
#    print(short_list [position])
#except IndexError as name:
#    print('bad index',position)
#    print('Need a position between 0 to ',len(short_list)-1,'but got ',position)

#class UppercaseException (Exception):   #??
#    pass

#words = ['eeenie','meenie','miny','Mo']
#for word in words:
#    if word.isupper():
#        raise UppercaseException(word)
