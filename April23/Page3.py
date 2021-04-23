#Operator Overloading

def function_1():
    num1 = 100
    num2 = 200

    print(f"num1 = {num1}, type = {type(num1)}")
    print(f"num2 = {num2}, type = {type(num2)}")

    # addition = int.__add__(num1, num2)
    # addition = num1.__add__(num2)
    addition = num1 + num2
    print(f"addition = {addition}")
    print(int.__dict__)


# function_1()


def function_2():
    str1 = "sunbeam"
    str2 = "institute"

    print(f"str1 = {str1}, type = {type(str1)}")
    print(f"str2 = {str2}, type = {type(str2)}")

    # addition = str.__add__(str1, str2)
    # addition = str1.__add__(str2)
    addition = str1 + str2
    print(f"addition = {addition}")
    print(str.__dict__)


# function_2()


class MyNumber:
    def __init__(self, number):
        self.__number = number

    def print_details(self):
        print(f"number = {self.__number}")

    def __add__(self, num2):
        return self.__number + num2.__number


def function_3():
    num1 = MyNumber(100)
    num2 = MyNumber(200)

    print(f"num1 = {num1}, type = {type(num1)}")
    print(f"num2 = {num2}, type = {type(num2)}")

    # addition = MyNumber.__add__(num1, num2)
    # addition = num1.__add__(num2)
    addition = num1 + num2
    print(f"addition = {addition}")


function_3()
