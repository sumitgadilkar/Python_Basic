def function_1():
    numbers = [1, 2, 3, 4, 5]
    for number in numbers:
        print(f"square of {number} = {number ** 2}")


# function_1()


def function_2():
    numbers = [1, 2, 3, 4, 5]

    # step 1: create an empty list
    squares = []

    # step 2: iterate over the collection
    for number in numbers:

        # step 3: perform the logic (square)
        #         add add the result to the list
        squares.append(number ** 2)

    print(f"squares = {squares}")


# function_2()


def calculate_square(number):
    print(f"inside calculate_square, number: {number}")
    return number ** 2


def function_3():
    numbers = [6, 7, 8, 9, 10]

    # map
    # call calculate_square function for every member inside the numbers list
    squares = list(map(calculate_square, numbers))
    print(f"squares = {squares}")


# function_3()


def function_4():
    numbers = [6, 7, 8, 9, 10]
    cube = lambda n: n ** 3
    cubes = list(map(cube, numbers))
    print(f"cubes = {cubes}")


# function_4()


def function_5():
    numbers = [6, 7, 8, 9, 10]

    cubes = list(map(lambda n: n ** 3, numbers))
    print(f"cubes = {cubes}")


# function_5()


def function_6():
    numbers = [1, 2, 3, 4, 5]

    # add 10 in every number
    result = list(map(lambda n: n + 10, numbers))
    print(f"result = {result}")


function_6()
