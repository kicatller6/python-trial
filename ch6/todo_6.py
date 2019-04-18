#6.1
class Thing:
    pass
example = Thing()
#print(Thing)
#print(example)
#6.2
class Thing2:
    letters = 'abc'
#print(Thing2.letters)
#6.3
class Thing3:
    def __init__(self):     #letters為實例屬性，非類別本身，沒有實例不能叫出
        self.letters = 'xyz'
example3 = Thing3()
#print(example3.letters)
#6.4
class Element:
    def __init__(self,name,symbol,number):
        self.__name = name
        self.__symbol = symbol
        self.__number = number
    def __str__(self):#6.7
        return 'name = %s,symbol = %s,number = %s'%(self.__name,self.__symbol,self.__number)
    def name (self):
        return self.__name
    def symbol (self):
        return self.__symbol
    def number (self):
        return self.__number    
example4 = Element('Hydrongen','H',1)
#print(example4)
#6.5
example5 = {'name':'Hydrongen','symbol':'H','number':1}
Hydrogen = Element(**example5)
#Hydrogen.dump()
#print(Hydrogen)
#6.8
#print(Hydrogen.name())
#6.9
class Bear():
    def eats(self):
        return 'berries'
class Rabbit():
    def eats(self):
        return 'clover'
class Octorthorpe():
    def eats(self):
        return 'campers'
#6.10
class Laser():
    def does(self):
        return 'distinttegrate'
class Claw():
    def does(self):
        return 'crush'
class Smartphone():
    def does(self):
        return 'ring'
class Robot():
    def __init__(self,Laser,Claw,Smartphone):
        self.Laser = Laser
        self.Claw = Claw
        self.Smartphone = Smartphone
    def does(self):
        print('Laser:%s'%(self.Laser.does()))
laser = Laser()
claw = Claw()
smart = Smartphone()
robot_L = Robot(laser,claw,smart)
robot_L.does()