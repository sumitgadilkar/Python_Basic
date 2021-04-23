class Person:
    def __init__(self, name, address):
        # protected members
        # - can be accessed in the same class
        # - can be accessed in the derived class(es)
        # - should not be accessed outside the class
        self._name = name
        self._address = address

    def print_person_details(self):
        print(f"name = {self._name}")
        print(f"address = {self._address}")

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name


class Employee(Person):
    def __init__(self, id, name, address):
        Person.__init__(self, name, address)
        self.__id = id

    def print_details(self):
        # self.print_person_details()
        print(f"name = {self._name}")
        print(f"address = {self._address}")
        print(f"id = {self.__id}")


e1 = Employee(1, "emp1", "pune")
print(f"e1 = {e1.__dict__}")
print(f"name = {e1.get_name()}")
e1.print_details()