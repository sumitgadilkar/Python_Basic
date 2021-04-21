# association

# Professor
# - name, address, subject
class Professor:
    def __init__(self, name, address, subject):
        self.__name = name
        self.__address = address
        self.__subject = subject

    def print_professor_details(self):
        print(f"| {self.__name:<20} | {self.__address:<20} | {self.__subject:<20} |")


# Department
# - name
class Department:
    def __init__(self, name):
        self.__name = name
        self.__professors = []

    def add_professor(self, name, address, subject):
        new_professor = Professor(name, address, subject)
        self.__professors.append(new_professor)

    def print_department_details(self):
        print(f"name = {self.__name}")
        print("--- professor details ---")
        for professor in self.__professors:
            professor.print_professor_details()


department = Department('Computer')
department.add_professor("professor 1", "pune", "Networking")
department.add_professor("professor 2", "mubmai", "OS")
department.add_professor("professor 3", "satara", "Python")
department.add_professor("professor 4", "nashik", "JS")
department.print_department_details()