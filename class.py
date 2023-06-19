class animal:
    def sound(self):
        print("sound")

class dog(animal):
   
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def bark(self): # For every function inside a class the first parameter has to be self
        print('Woof!')

rex = dog('Rex',12)
print(rex.name , rex.age)
rex.bark()

rex.sound()
