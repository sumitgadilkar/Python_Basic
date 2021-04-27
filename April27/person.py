class Person:
    def __init__(self, name, address):
        self._name = name
        self._address = address

    def __str__(self):
        return f"Person [name: {self._name}, address: {self._address}]"


class Player(Person):
    def __init__(self, name, address, team):
        Person.__init__(self, name, address)
        self.__team = team

    def __str__(self):
        return f"Player [name: {self._name}, address: {self._address}, team: {self.__team}]"


if __name__ == "__main__":
    person1 = Person("person1", "pune")
    print(person1)