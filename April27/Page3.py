print(f"name of the page4 module = {__name__}")


def function1():
    # import the whole module
    import math

    num1 = int(input("enter first number: "))
    num2 = int(input("enter second number: "))
    math.add(num1, num2)
    math.divide(num1, num2)
    math.multiply(num1, num2)
    math.subtract(num1, num2)


# function1()


def function2():
    # import only add function from math module
    from math import add

    num1 = int(input("enter first number: "))
    num2 = int(input("enter second number: "))

    add(num1, num2)


# function2()


def function3():
    # import the whole module with an alias of my_math
    import math as my_math

    num1 = int(input("enter first number: "))
    num2 = int(input("enter second number: "))

    my_math.add(num1, num2)


# function3()


def function4():
    # import only add function with an alias my_add from math module
    from math import add as my_add             #--------------------------ALIAS

    num1 = int(input("enter first number: "))
    num2 = int(input("enter second number: "))

    my_add(num1, num2)


function4()


def function5():
    from math import divide

    # import math
    # print(f"contents of math: {dir(math)}")

    divide(10, 5)


# function5()
