class InvalidAge(Exception):
    pass

def function_23():
        name = input("Enter your name")
        address = input("Enter your address")
        age = int(input("Enter your age"))

        if (age<25) or (age>99):
            raise InvalidAge()

        else:
            print(f"name = {name}")
            print(f"address = {address}")
            print(f"age = {age}")

try:
    function_23()
except InvalidAge:
    print(f"This is an Invalid age")

