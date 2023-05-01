# we are expecting a int parameter and returning a string 
def myfucntion(myparameter: int) -> str:
    # print(myparameter)
    return f'{myparameter +10}'

# as python in dynamically typed langusge it still allows 
# string argument even tho it is mentioned int
# myfucntion("Hello world")
# print(myfucntion(10))

def otherfunction(otherparameter: str):
    print(otherparameter)

def dosomth(param: list[int]):
    print(param)

# otherfunction(myfucntion(10))
# dosomth([1,2,3])
dosomth(['s'])