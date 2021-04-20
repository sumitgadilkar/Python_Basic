#OOPS

# empty class
class Person:
    """
    this is a dummy class
    """
    pass


# create an object of Person
p = Person()

# Person will have following attributes
# name, address, age

print(p.__dict__)

# add/set an attribute in an object
setattr(p, "name", "person1")
setattr(p, "address", "pune")
setattr(p, "age", 30)
setattr(p, "computer", True)

# print(Person.__doc__)
print(p.__dict__)

print(f"name = {getattr(p, 'name')}")
print(f"address = {getattr(p, 'address')}")
print(f"age = {getattr(p, 'age')}")


# create a new object of type Person
p2 = Person()
print(f"p2 = {p2.__dict__}")
setattr(p2, "full_name", "person2")
print(f"p2 = {p2.__dict__}")

p3 = p
print(f"p3 = {p3.__dict__}")