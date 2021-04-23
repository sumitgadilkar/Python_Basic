#Multiple Inheritance

class Faculty:
    def __init__(self, name, subject):
        self._name = name
        self._subject = subject

    def print_details(self):
        print("=== Faculty details ===")
        print(f"name = {self._name}")
        print(f"subject = {self._subject}")


class LabAssistant:
    def __init__(self, name, lab):
        self._name = name
        self._lab = lab

    def print_details(self):
        print("=== LabAssistant details ===")
        print(f"name = {self._name}")
        print(f"lab = {self._lab}")


class FacultyLabAssistant(Faculty, LabAssistant):
    def __init__(self, name, subject, lab):
        Faculty.__init__(self, name, subject)
        LabAssistant.__init__(self, name, lab)

    def print_details(self):
        print("=== FacultyLabAssistant details ===")
        print(f"name = {self._name}")
        print(f"lab = {self._lab}")
        print(f"subject = {self._subject}")


faculty_lab_assistant = FacultyLabAssistant("faculty1", "computer", "computer-lab")
faculty_lab_assistant.print_details()
print(f"base class for FacultyLabAssistant = {FacultyLabAssistant.__bases__}")

##############
##############

class Developer:
    pass


class Tester:
    pass


class DeveloperTester(Developer, Tester):
    pass


class Operations:
    pass


class DevOps(Developer, Operations):
    pass
