def function1():
    # list of numbers (int)
    numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    print(f"numbers type = {type(numbers)}")

    for number in numbers:
        print(number)


# function1()


def function2():
    # list of numbers (int)
    numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    print(f"numbers type = {type(numbers)}")

    # iterator iterates on iterable
    iterator = iter(numbers)
    print(f"iterator: {iterator}")

    try:
        print(f"value = {next(iterator)}")
        print(f"value = {next(iterator)}")
        print(f"value = {next(iterator)}")
        print(f"value = {next(iterator)}")
        print(f"value = {next(iterator)}")
        print(f"value = {next(iterator)}")
        print(f"value = {next(iterator)}")
        print(f"value = {next(iterator)}")
        print(f"value = {next(iterator)}")
        print(f"value = {next(iterator)}")
        print(f"value = {next(iterator)}")
        print(f"value = {next(iterator)}")
        print(f"value = {next(iterator)}")
        print(f"value = {next(iterator)}")
        print(f"value = {next(iterator)}")
    except StopIteration:
        print("end of numbers collection")


function2()


def function3():
    # list of numbers (int)
    numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    for index in range(0, len(numbers), 2):
        print(f"value at {index} = {numbers[index]}")


# function3()