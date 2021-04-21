# 1 company with many employee relationship

class Employee:
    def __init__(self, id, name, email, salary):
        self.__id = id
        self.__name = name
        self.__email = email
        self.__salary = salary

    def print_employee_details(self):
        # print(f"id = {self.__id}")
        # print(f"name = {self.__name}")
        # print(f"email = {self.__email}")
        # print(f"salary = {self.__salary}")
        print(f"| {self.__id:^3} | {self.__name:<15} | {self.__email:<15} | {self.__salary:^10} |")


# association
# 1 company may have many employees
class Company:
    def __init__(self, name, address):
        self.__name = name
        self.__address = address

        # empty list to hold the future employees
        self.__employees = []

    def add_employee(self, name, email, salary):
        # generate id for the employee automatically
        id = len(self.__employees) + 1
        new_employee = Employee(id, name, email, salary)

        # add employee to the company's employee list (payrole)
        self.__employees.append(new_employee)

    def print_company_details(self):
        print(f"name = {self.__name}")
        print(f"address = {self.__address}")
        print(f"--- employees information ---")
        for employee in self.__employees:
            employee.print_employee_details()


company = Company("company1", "pune")
company.add_employee("employee1", "emp1@test.com", 10000)
company.add_employee("employee2", "emp2@test.com", 15000)
company.add_employee("employee3", "emp3@test.com", 20000)
company.add_employee("employee4", "emp4@test.com", 40000)
company.add_employee("employee5", "emp5@test.com", 60000)
company.print_company_details()