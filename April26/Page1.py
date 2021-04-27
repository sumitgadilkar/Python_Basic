#Exception Handling:

def function_1():
    try:
        # this code will be first tried out
        str1 = input("enter a number: ")
        int_str1 = int(str1)
        print(f"int_str1 = {int_str1}, type = {type(int_str1)}")
    except:
        # used to catch error/exception
        # used to handle the error
        # once the error is handled, it wont reach to PVM, which results in
        # non-crashing of the application
        print(f"application has received an error")
        # pass


# function_1()


def function_2():
    try:
        n1 = int(input("enter first number: "))
        n2 = int(input("enter second number: "))
        division = n1 / n2
    except ValueError as error:
        print("invalid number(s), please try again")
        print(f"error = {error}")
    except ZeroDivisionError as error:
        print("denominator can not be zero")
        print(f"error = {error}")
    except:
        # generic except block
        print("some other error")
    else:
        print(f"{n1} / {n2} = {division}")


function_2()