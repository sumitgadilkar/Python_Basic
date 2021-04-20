# Student
# - name, school, roll_no, address, age, marks
# - print_details, print_result

class Student:

    def __init__(self, name, address, age, roll_no, school, marks):
        self.__name = name
        self.__address = address
        self.__age = age
        self.__roll_no = roll_no
        self.__school = school
        self.__marks = marks

    def print_details(self):
        print(f"name: {self.__name}")
        print(f"address: {self.__address}")
        print(f"age: {self.__age}")
        print(f"roll_no: {self.__roll_no}")
        print(f"school: {self.__school}")
        print(f"marks: {self.__marks}")

    def print_result(self):
        if self.__marks >= 50:
            print("congrats!!! you have passed in the exam")
        else:
            print("oops!!! you have failed in the exam")


s1 = Student("student1", "pune", 16, 1, "school 1", 80)
s1.print_details()
s1.print_result()

# Person
# - name, address, age
# - print_details