#Raising an error ; Customer error:
class InvalidAgeError(Exception):
    # custom exception/error class
    pass


def function_1():
    name = input("enter your name: ")
    address = input("enter your address: ")
    age = int(input("enter your age: "))
    if (age < 25) or (age > 60):
        # generate an error
        raise InvalidAgeError()

    print(f"name = {name}")
    print(f"address = {address}")
    print(f"age = {age}")


try:
    function_1()
except InvalidAgeError:
    print(f"age is invalid")