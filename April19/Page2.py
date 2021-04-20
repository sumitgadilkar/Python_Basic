class Person:

    # method
    def init_person(self, name, address, age):
        setattr(self, "name", name)
        setattr(self, "address", address)
        setattr(self, "age", age)

    # self is nothing but "this" in another languages
    def print_details(self):
        print(f"name: {getattr(self, 'name')}")
        print(f"address = {getattr(self, 'address')}")
        print(f"age = {getattr(self, 'age')}")

    def can_vote(self):
        age = getattr(self, "age")
        if age >= 18:
            print(f"{getattr(self, 'name')} is eligible for voting")
        else:
            print(f"{getattr(self, 'name')} is NOT eligible for voting")


# create an object
p1 = Person()
p1.init_person("person1", "pune", 20)

# PoP: Procedure oriented Programming
# print_details(p1)
# OOP: Object Oriented Programming
# 0x10000 (0x50000)
# print_details(p1)
p1.print_details()

p1.can_vote()
print(p1.__dict__)
print(Person.__dict__)
print("-" * 50)

p2 = Person()
p2.init_person("person2", "mumbai", 10)
# print_details(p2)
p2.print_details()
p2.can_vote()
print(p2.__dict__)
print(Person.__dict__)
print("-" * 50)


def print_details(num):
    print(f"num = {num}")


# 0x80000 (10)
print_details(10)