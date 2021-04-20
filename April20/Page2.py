class Car:
    # initializer
    def __init__(self, model, company, price):
        self.__model = model
        self.__company = company
        self.__price = price

    # de-initializer
    def __del__(self):
        print(f"inside de-initializer for {self.__model}")

    # facilitators
    def print_details(self):
        print(f"model = {self.__model}")
        print(f"company = {self.__company}")
        print(f"price = {self.__price}")

    def is_affordable(self):
        if self.__price <= 10:
            print(f"Yes.. {self.__model} is affordable")
        else:
            print(f"No.. {self.__model} is NOT affordable")

    # setters
    def set_price(self, price):
        self.__price = price

    def set_model(self, model):
        self.__model = model

    def set_company(self, company):
        self.__company = company

    # getters
    def get_model(self):
        return self.__model

    def get_company(self):
        return self.__company

    def get_price(self):
        return self.__price


c1 = Car("i20", "hyundai", 7.5)
c1.print_details()
c1.is_affordable()

# delete c1 as its not needed any more
del c1

c2 = Car("X5", "BMW", 49)
print(f"company: {c2.get_company()}")
# c2.print_details()