class Student:
    def __init__(self, roll_no, name, standard):
        self.__roll_no = roll_no
        self.__name = name
        self.__standard = standard

    def __str__(self):
        return f"Student [roll no: {self.__roll_no}, name: {self.__name}, standard: {self.__standard}]"


class School:
    def __init__(self, name):
        self.__name = name
        self.__students = []
        self.__index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__index >= len(self.__students):
            raise StopIteration()

        student = self.__students[self.__index]
        self.__index += 1
        return student

    def add_student(self, name, standard):
        roll_no = len(self.__students) + 1
        student = Student(roll_no, name, standard)
        self.__students.append(student)

    def print_details(self):
        print(f"name = {self.__name}")
        print(f"--- students ---")
        for student in self.__students:
            print(student)


school = School("school 1")
school.add_student("student 1", "I")
school.add_student("student 2", "I")
school.add_student("student 3", "I")
school.add_student("student 4", "I")
school.add_student("student 5", "I")
# school.print_details()

# School.__iter__(school)
# school.__iter__()
iterator = iter(school)
print(f"iterator = {iterator}")

# School.__next__(school)
# school.__next__()
# iterator.__next__()
# print(f"student = {next(iterator)}")
# print(f"student = {next(iterator)}")
# print(f"student = {next(iterator)}")
# print(f"student = {next(iterator)}")
# print(f"student = {next(iterator)}")
# print(f"student = {next(iterator)}")

for student in school:
    print(student)