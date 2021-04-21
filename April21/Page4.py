
#Inheritance example -> IS A relationship
class Person:
    def __init__(self):
        self.name = ""
        self.address = ""
        self.age = 0


# Student is-a Person
# Student inherits Person
# Student is inherited from Person
# Student is derived from Person
class Student(Person):
    pass


# p1 = Person()
# print(f"p1 = {p1.__dict__}")

s1 = Student()
print(f"s1 = {s1.__dict__}")


class Employee:
    def __init__(self, name, address, age):
        self.__name = name
        self.__address = address
        self.__age = age


class Company:
    def __init__(self, name, address):
        self.__name = name
        self.__address = address
        self.__employee = None

    def add_emp(self, name, address, age):
        self.__employee = Employee(name, address, age)


company = Company("c1", "a1")
company.add_emp("emp1", "emp_add1", 25)