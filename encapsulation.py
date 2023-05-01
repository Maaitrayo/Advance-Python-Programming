class Person:
    def __init__(self, name, age, gender):
        # private attributes
        self.__name = name
        self.__age = age
        self.__gender = gender

    @property
    def Name(self):
        return self.__name
    
    # python does not allow function overloadding 
    @Name.setter
    def Name(self, value):
        if value == "Bob":
            self.__name = "Default Name"
        else:
            self.__name = value
    
    @staticmethod
    def mymethod():
        print("Hello World!")

# calling mymethod without creating any object as it is a static method 
Person.mymethod()

p1= Person("Maaitrayo", 20, 'M')
print(p1.Name)

p1.Name = "Bob"
print(p1.Name)
