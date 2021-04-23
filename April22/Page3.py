#Private members in Parent/Base CLass and acccessing them Name_Mangling (hiding info) is seen in result
#e1 = {'_Person__name': 'emp1', '_Person__address': 'pune', '_Employee__id': 1} here name add age is name mangled
#used print_details to print name add and age
class Person:
    def __init__(self, name, address):
        self.__name = name
        self.__address = address

    def print_person_details(self):
        print(f"name = {self.__name}")
        print(f"address = {self.__address}")


class Employee(Person):
    def __init__(self, id, name, address):
        Person.__init__(self, name, address)
        self.__id = id

    def print_details(self):
        self.print_person_details()
        print(f"id = {self.__id}")


e1 = Employee(1, "emp1", "pune")
print(f"e1 = {e1.__dict__}")
e1.__id = -1
e1.print_details()