#what's obj:
num = 7
class Car():
    def __init__(self,name):
        self.name = name
    def exclaim(self):
        print('I\'m a car')
class Yugo(Car):
    def need_A_Push(self):
        print("A little help here?")
    def exclaim(self):
        print('I\'m a Yugo')
c = Car('bingo')
y = Yugo('march')

class person():
    def __init__(self,name):
        self.name = name
    def exclaim(self):
        print('I\'m a ',self.name)
class MDperson(person):
    def __init__(self,name):
        self.name = 'Doctor '+name
class JDperson(person):
    def __init__(self,name):
        self.name = name +',Esquire'
class EmailPerson(person):
    def __init__(self,name,email):
        super().__init__(name)
        self.email = email

MD = MDperson('nickolas')
EM = EmailPerson('Mike','mike@gmail')
#Car.exclaim(c)

class Duck():
    def __init__(self,input_name):
        self.__name = input_name
    @property    
    def name(self):
        #print('inside the getter')
        return self.__name
    @name.setter
    def name(self,input_name):
        print('inside the setter')
        self.__name = input_name
    #name = property(get_name,set_name)
ddt = Duck('Gra Gra')
#ddt.__name = ('Lu Lala')
#print(ddt.name)

class Circle():
    def __init__(self,radius):
        self.radius = radius
    @property
    def diameter(self):
        return 2*self.radius
circle = Circle(10)
#print(circle.diameter)
circle.radius = 5
#print(circle.diameter)

class A():
    count = 0
    def __init__(self):
        A.count +=1
    def exclaim(self):
        print('I\'m an A')
    @classmethod                #參照類別本身
    def kids(cls):
        print("A has",cls.count,"little object")
easy_a = A()
breezy_a = A()
wheezy_a = A()
#A.kids()

class coyoteWeapon():
    @staticmethod               #不用實例也可以呼叫
    def commercial():
        print('\nThis CoyoteWeapon has been brought to you by Acme\n')

#coyoteWeapon.commercial()

class Quote():
    def __init__(self,person,words):
        self.person = person
        self.words = words
    def who(self):
        return self.person
    def says(self):
        return self.words
class QuestionQuote(Quote):
    def says(self):
        return self.words +"?"
class ExclamationQuote(Quote):
    def says(self):
        return self.words+"!"

class BabblingBrook():
    def who(self):
        return 'Brook'
    def says(self):
        return 'Babble'
hunter = Quote('Elmer',"I'm hunting wabbits")
hunted1 = QuestionQuote('Bunny',"What's up ,doc")
hunted2 = ExclamationQuote("Duck","It's rabbits season")
brook = BabblingBrook()
def who_says(obj):
    print (obj.who(),'says',obj.says())
#who_says(brook)
#who_says(hunter)
#who_says(hunted1)
#who_says(hunted2)
class word():
    def __init__(self,text):
        self.text = text
    def __eq__(self,word2):
        return self.text.lower() == word2.text.lower()
    def __ne__(self,word2):
        return self.text.lower() == word2.text.lower()
    def __str__(self):
        return self.text
    def __repr__(self):
        return 'Word("'+self.text+'")'
#first = word('ha')
#second = word('Ha')
#print(first)    #use str

class Bill():
    def __init__(self,description):
        self.description = description
class Tail():
    def __init__(self,length):
        self.length = length
class Sparrow():
    def __init__(self,bill,tail):
        self.bill = bill
        self.tail = tail
    def about(self):
        print('This duck has a',self.bill.description,'bill and a',
        self.tail.length,'tail')

tail = Tail('long')
bill = Bill('wide orange')
spw = Sparrow(bill,tail)
#spw.about()

from collections import namedtuple      #酷~
Duc = namedtuple('Duck','bill tail')
duc = Duc('wide orange','long')
duc2 = duc._replace(tail='manificient',bill = 'crushing')
print(duc2)
