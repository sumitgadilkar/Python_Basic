def function_1():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    squares = list(map(lambda n: n ** 2, numbers))
    cubes = list(map(lambda n: n ** 3, numbers))

    print(f"numbers = {numbers}")
    print(f"squares = {squares}")
    print(f"squares = {cubes}")


# function_1()


def function_2():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    even_numbers = list(filter(lambda n: n % 2 == 0, numbers))
    odd_numbers = list(filter(lambda n: n % 2 != 0, numbers))

    print(f"numbers = {numbers}")
    print(f"even numbers = {even_numbers}")
    print(f"odd numbers = {odd_numbers}")


# function_2()


def function_3():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # find even numbers
    # filter returns an iterable object
    even_numbers = filter(lambda n: n % 2 == 0, numbers)
    # print(f"even numbers = {even_numbers}")

    # find square of every even number
    square_even_numbers = tuple(map(lambda n: n ** 2, even_numbers))

    print(f"numbers = {numbers}")
    print(f"square of even numbers = {square_even_numbers}")


# function_3()


def function_4():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # cube of odd numbers
    odd_numbers = filter(lambda n: n % 2 != 0, numbers)

    # find cube of every odd number
    cube_odd_numbers = tuple(map(lambda n: n ** 3, odd_numbers))
    print(f"numbers = {numbers}")
    print(f"cube of odd numbers = {cube_odd_numbers}")


function_4()