#__init__ : initilizer method to initilaize object
class Car:

    # initializer
    def __init__(self, model, company, price):
        print(f"inside __init__ method")
        setattr(self, 'model', model)
        setattr(self, 'company', company)
        setattr(self, 'price', price)

    def print_details(self):
        print(f"model: {getattr(self, 'model')}")
        print(f"company: {getattr(self, 'company')}")
        print(f"price: {getattr(self, 'price')}")


# allocates the memory
# call __init__
c1 = Car("i20", "hyundai", 7.5)
c1.print_details()

# allocates the memory
# call __init__
c2 = Car("fabia", "skoda", 6.5)
c2.print_details()


# Default parameter in method:
class Car:

    # initializer
    def __init__(self, model='', company='', price=0):
        print(f"inside __init__ method")
        setattr(self, 'model', model)
        setattr(self, 'company', company)
        setattr(self, 'price', price)

    def print_details(self):
        print(f"model: {getattr(self, 'model')}")
        print(f"company: {getattr(self, 'company')}")
        print(f"price: {getattr(self, 'price')}")


# allocates the memory
# call __init__
c1 = Car() # no parameter passes so
c1.print_details()

# allocates the memory
# call __init__
c2 = Car("fabia", "skoda", 6.5)
c2.print_details()