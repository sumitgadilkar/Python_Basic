#List comprehension

def function_1():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # attempt 1
    squares_1 = []
    for number in numbers:
        squares_1.append(number ** 2)

    # attempt 2
    squares_2 = list(map(lambda n: n ** 2, numbers))
    print(f"squares_1 = {squares_1}, squares_2 = {squares_2}")


# function_1()


def function_2():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # list of square of every number in numbers collection
    # list comprehension as map
    squares = [number ** 2 for number in numbers]
    print(f"squares = {squares}")


# function_2()


def function_3():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    cubes = [n ** 3 for n in numbers]
    print(f"cubes = {cubes}")


# function_3()


def function_4():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # attempt 1
    even_numbers_1 = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers_1.append(number)

    # attempt 2
    even_numbers_2 = list(filter(lambda n: n % 2 == 0, numbers))
    print(f"even_numbers_1 = {even_numbers_1}, even_numbers_2 = {even_numbers_2}")


# function_4()


def function_5():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # list of even numbers
    # even_numbers = [n for n in filter(lambda n: n % 2 == 0, numbers)]
    # list comprehension as filter
    even_numbers = [n for n in numbers if n % 2 == 0]
    print(f"even_numbers = {even_numbers}")


# function_5()


def function_6():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # square of even numbers
    square_even_numbers = [n ** 2 for n in numbers if n % 2 == 0]

    # cube of odd numbers
    cube_odd_numbers = [n ** 3 for n in numbers if n % 2 != 0]

    print(f"square_even_numbers = {square_even_numbers}")
    print(f"cube_odd_numbers = {cube_odd_numbers}")


# function_6()


def function_6():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    squares = tuple(n ** 2 for n in numbers)
    even_numbers = tuple(n for n in numbers if n % 2 == 0)
    square_even_numbers = tuple(n ** 2 for n in numbers if n % 2 == 0)

    print(f"numbers = {numbers}")
    print(f"squares = {squares}")
    print(f"even_numbers = {even_numbers}")
    print(f"square_even_numbers = {square_even_numbers}")


# function_6()


def function_7():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # [(1, 1), (2, 4), (3, 9), ...]
    squares = map(lambda n: n ** 2, numbers)
    result_1 = list(zip(numbers, squares))
    print(f"result_1 = {result_1}")

    # list comprehension as a zip
    result_2 = [(n, n ** 2) for n in numbers]
    print(f"result_2 = {result_2}")


function_7()