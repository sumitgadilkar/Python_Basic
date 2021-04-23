class Person:
    def __init__(self, name, address, age):
        self.name = name
        self.address = address
        self.age = age

    def print_person_details(self):
        print(f"name = {self.name}")
        print(f"address = {self.address}")
        print(f"age = {self.age}")

    def can_vote(self):
        if self.age >= 18:
            print(f"Yes. {self.name} is eligible for voting")
        else:
            print(f"No. {self.name} is not eligible for voting")


class Employee(Person):
    def __init__(self, id, company, name, address, age):
        Person.__init__(self, name, address, age)
        self.id = id
        self.company = company

    def print_details(self):
        print(f"--- employee details ---")

        # Employee.print_person_details(self)
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

# Employee.print_details(e1)
e1.print_details()
print(f"Person = {Person.__dict__}")
print(f"Employee = {Employee.__dict__}")

p1 = Player("player1", "mumbai", 30, "india")
p1.print_details()
print(f"Player = {Player.__dict__}")


# allocate new memory for person1
# Person.__init__(person1, "person1", "satara", 10)
person1 = Person("person1", "satara", 10)

# Person.print_person_details(person1)
person1.print_person_details()

# Person.can_vote(person1)
person1.can_vote()