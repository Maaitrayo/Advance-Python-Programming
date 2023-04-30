def myDecorator(function):
    def wrapper(*args,**kwargs):
        return_value = function(*args,**kwargs)
        print("I am decorating your function!")
        return return_value
    
    return wrapper

@myDecorator
def hello_world(person):
   print(f"Hello {person}!")
   return f"Hello {person}!"

# print(hello_world("Maaitrayo"))

'''Practical example 1'''
def logged(function):
    def wrapper(*args, **kwargs):
        value = function(*args, **kwargs)
        with open('logfile.txt', 'a+') as f:
            fname = function.__name__
            print(f'{fname} returned value {value}')
            f.write(f'{fname} returned value {value}\n')
        return value
    return wrapper

@logged
def add(x,y):
    return x+y
# print(add(10,20))

'''Practical Example 2'''
import time

def timmed(function):
    def wrapper(*args,**kwargs):
        before = time.time()
        result = function(*args,**kwargs)
        after = time.time()
        fname = function.__name__
        print(f'{fname} took {after-before} seconds to execute')
        return result
    return wrapper

@timmed
def myFunction(x):
    result = 1
    for i in range(1,x):
        result *= i
    return result

# print(myFunction(10000))
myFunction(100000)