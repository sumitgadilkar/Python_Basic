def function_1():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    squares = list(map(lambda n: n ** 2, numbers))
    print(f"numbers = {numbers}")
    print(f"squares = {squares}")

    number_squares = list(zip(numbers, squares))
    print(f"number and square of numbers = {number_squares}")


function_1()


def function_2():
    numbers_1 = [1, 2, 3, 4, 5]
    numbers_2 = [6, 7, 8, 9, 10]

    # list of tuples
    # [(1, 6), (2, 7), (3, 8), (4, 9), (5, 10)]
    result = []

    # [0, 1, 2, 3, 4]
    for index in range(len(numbers_1)):
        result.append((numbers_1[index], numbers_2[index]))

    print(f"result = {result}")


# function_2()


def function_3():
    numbers_1 = [1, 2, 3, 4, 5]
    numbers_2 = [6, 7, 8, 9, 10]

    result = list(zip(numbers_1, numbers_2))
    print(f"result = {result}")


# function_3()


def function_4():
    numbers_1 = [1, 2, 3, 4, 5]
    numbers_2 = [6, 7, 8, 9, 10]
    numbers_3 = [11, 12, 13, 14, 15]

    result = tuple(zip(numbers_1, numbers_2, numbers_3))
    print(f"result = {result}")


# function_4()
