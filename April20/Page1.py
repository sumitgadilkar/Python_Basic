class Person:
    def __init__(self, name, address, age):
        # if an attribute is declared with a prefix:
        # - no underscore   : public member
        #   - can be modified outside of a class
        # - one underscore  : protected member
        # - two underscores : private member
        #   - can be accessed only within the same class
        #   - can not be accessed/modified outside the class
        self.name = name
        self.address = address
        self.__age = age

    def print_details(self):
        print(f"name = {self.name}")
        print(f"address = {self.address}")
        print(f"age = {self.__age}")
        print()

        # setter method
    def set_age(self, age):
        if (age > 25) and (age < 60):
            self.__age = age
        else:
            print("invalid age. please use a valid value")



p1 = Person("person1", "pune", 30)
p1.print_details()
p1.name = "invalid name"
p1.address = "invalid address"
p1.__age = -100                      #---------> Not able to change value of age as it is protected
print(p1.__dict__)
p1.print_details()
