#Association:
# association

class Employee:
    def __init__(self, name, email, salary):
        self.__name = name
        self.__email = email
        self.__salary = salary

    def print_employee_details(self):
        print(f"name = {self.__name}")
        print(f"email = {self.__email}")
        print(f"salary = {self.__salary}")


# association
# aggregation: loose coupling
# 1 company has only 1 employee
class Company:
    def __init__(self, name, address):
        self.__name = name
        self.__address = address

        # employee information will be set later
        self.__employee = None

    def set_employee(self, name, email, salary):
        # create a new object to store employee details
        self.__employee = Employee(name, email, salary)

    def print_company_details(self):
        print(f"name = {self.__name}")
        print(f"address = {self.__address}")
        print(f"--- employee details ---")
        self.__employee.print_employee_details()


company = Company("company1", "pune")
company.set_employee("employee1", "emp1@test.com", 10000)
company.print_company_details()