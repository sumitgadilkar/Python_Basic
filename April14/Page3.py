#Filter

def function_1():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # find the even numbers
    for number in numbers:
        # check if the number is even
        if number % 2 == 0:
            print(f"{number} is even")


# function_1()


def function_2():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # empty list to collect even numbers
    even_numbers = []

    # find the even numbers
    for number in numbers:

        # check if the number is even
        if number % 2 == 0:
            even_numbers.append(number)

    print(f"even numbers = {even_numbers}")


# function_2()

def is_even_number(number):
    print(f"inside is_even_number, number: {number}")

    # check if the number is even
    return number % 2 == 0


def function_3():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # select number where number is even
    even_numbers = list(filter(is_even_number, numbers))
    print(f"even_numbers = {even_numbers}")


# function_3()


def function_4():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    is_odd = lambda n: n % 2 != 0
    odd_numbers = list(filter(is_odd, numbers))
    print(f"odd_numbers = {odd_numbers}")


# function_4()

