def function1():
    import person
    person1 = person.Person("person1", "pune")
    print(person1)


# function1()

def function2():
    from person import Player
    player1 = Player("player1", "pune", "india")
    print(player1)


# function2()


def function3():
    import person as my_person
    person1 = my_person.Person("person1", "pune")
    print(person1)


# function3()


def function4():
    from person import Player as MyPlayer
    player1 = MyPlayer("player1", "pune", "india")
    print(player1)


function4()