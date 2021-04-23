class Person:
    def __init__(self, name, address, age):
        self.name = name
        self.address = address
        self.age = age

    def print_person_details(self):
        print(f"name = {self.name}")
        print(f"address = {self.address}")
        print(f"age = {self.age}")


class Employee(Person):
    def __init__(self, id, company, name, address, age):
        Person.__init__(self, name, address, age)
        self.id = id
        self.company = company

    def print_details(self):
        print(f"--- employee details ---")
        self.print_person_details()
        print(f"id = {self.id}")
        print(f"company = {self.company}")
        print(f"--- employee details ---")
        print()


class Player(Person):
    def __init__(self, name, address, age, team):
        Person.__init__(self, name, address, age)
        self.team = team

    def print_details(self):
        print(f"--- Player details ---")
        self.print_person_details()
        print(f"team = {self.team}")
        print(f"--- Player details ---")
        print()


e1 = Employee(1, "company1", "emp1", "pune", 30)
e1.print_details()

p1 = Player("player1", "mumbai", 30, "india")
p1.print_details()