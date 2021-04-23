#MUltilevel inheritance:

class Person:
    def __init__(self, name):
        self._name = name

    def print_person_details(self):
        print(f"name = {self._name}")


class Employee(Person):
    def __init__(self, id, name):
        Person.__init__(self, name)
        self._id = id

    def print_employee_details(self):
        print(f"id = {self._id}")
        print(f"name = {self._name}")


class Manager(Employee):
    def __init__(self, id, name, department):
        Employee.__init__(self, id, name)
        self._department = department

    def print_manager_details(self):
        print(f"id = {self._id}")
        print(f"name = {self._name}")
        print(f"department = {self._department}")


