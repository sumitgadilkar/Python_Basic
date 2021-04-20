# Functions:

def add_1(func):
    def add_2():
        return(func(1+2))
    return add_2


print(add_1(3))
