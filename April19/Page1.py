#transition from POP to OOP: Now Class has nothing as all functions are outside class
class Person:
    pass


def init_person(person, name, address, age):
    setattr(person, "name", name)
    setattr(person, "address", address)
    setattr(person, "age", age)


def print_details(person):
    print(f"name: {getattr(person, 'name')}")
    print(f"address = {getattr(person, 'address')}")
    print(f"age = {getattr(person, 'age')}")


def can_vote(person):
    age = getattr(person, "age")
    if age >= 18:
        print(f"{getattr(person, 'name')} is eligible for voting")
    else:
        print(f"{getattr(person, 'name')} is NOT eligible for voting")


p1 = Person()
init_person(p1, "person1", "pune", 20)
print_details(p1)
can_vote(p1)

print('-' * 80)

p2 = Person()
init_person(p2, "person2", "mumbai", 10)
print_details(p2)
can_vote(p2)

print('-' * 80)

p3 = Person()
init_person(p3, "person3", "satara", 30)
print_details(p3)
can_vote(p3)


print('-' * 80)

# print_details(60)