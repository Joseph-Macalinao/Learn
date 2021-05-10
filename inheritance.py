'''
inheritance used for different classes if the same function or code is used in both
class Dog:
    def walk(self):
        print("walk")

class Cat:
    def walk(self):
        print('walk')

above is bad, don't repeat code
DRY
D-don't
R-repeat
Y-yourself



'''

class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    #cannot leave class empty, so either give its own function or pass
    def bark(self):
        print('bark')


class Cat(Mammal):
    def meow(self):
        print('meow')


cat1 = Cat()
cat1.meow()

