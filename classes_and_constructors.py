'''
classes used as way to create own interpretation of complex ideas
uses Pascal naming method (first letter of each word capitalized with no spaces(NoSpacesAllCaps))

class Point:
    def move(self):
        print('move')

    def draw(self):
        print('draw')


#objects - instance of a class used differently
point1 = Point()
point1.draw()

#attributes - variables that exist only for specific objects
point1.x = 10
point1.y = 20
print("(" + str(point1.x) + ',' + str(point1.y) + ')')

point2 = Point()
#x does not exist for point2 yet
point2.x = 4
#now it does

#constructors - function that gets called at time of creating an object
def __init__ used to construct objects
'''

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print('move')

    def draw(self):
        print('draw')


point = Point(10, 20)
point.x = 11
print(point.x)