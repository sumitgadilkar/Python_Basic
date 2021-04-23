#Method overriding base class using derived class

class Person:
    def __init__(self, name, address):
        self._name = name
        self._address = address

    def print_details(self):
        print(f"--person details--")
        print(f"name = {self._name}")
        print(f"address = {self._address}")


class Employee(Person):
    def __init__(self, id, name, address):
        Person.__init__(self, name, address)
        self._id = id

    def print_details(self):
        print(f"--employee details--")
        print(f"id = {self._id}")
        Person.print_details(self)


e1 = Employee(1, "employee1", "pune")
e1.print_details()

print()

p1 = Person("person1", "mumbai")
p1.print_details()

print()

print(f"base class for Employee = {Employee.__base__}")