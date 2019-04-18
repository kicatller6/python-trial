class Bear(object):
    def sound(self):
        print ("Groarrr")
 
class Dog(object):
    def sound(self):
        print ("Woof woof!")

def makeSound(object):
    object.sound()
 
bearObj = Bear()
dogObj = Dog()
makeSound(bearObj)
makeSound(dogObj)
