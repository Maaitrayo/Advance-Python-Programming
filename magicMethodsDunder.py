class Person:
    # constructor
    def __init__(self, name,age):
        self.name = name
        self.age = age
    
    # Deconstructor
    def __del__(self):
        print("object is being deconstructed!")
    
# p = Person("Maaitrayo", 25)

'''First part of tutorial ends'''

class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def __add__(self,other):
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"X: {self.x}, Y: {self.y}"
    
    def __len__(self):
        return 10
    
    def __call__(self):
        print("Hello I was called !")

v1 = Vector(10,20)
v2 = Vector(50,60)
v3 = v1+v2
# print(v3.x, v3.y)
# print(len(v3))
v3()