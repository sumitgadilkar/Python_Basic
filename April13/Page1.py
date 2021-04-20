# Unicode Transformation Format
# UTF-8 : 8 bit or 1 byte   : 256 characters
# UTF-16: 16 bits or 2 bytes: 65536 characters

def function_1():
    # string: collection of unicode characters
    str_1 = "This Is A    Test   String 1"

    print(f"str_1 = {str_1}")
    print(f"all caps = {str_1.upper()}")
    print(f"all lower = {str_1.lower()}")
    print(f"len of str_1 = {len(str_1)}")


# function_1()


def function_2():
    # string: collection of characters
    str_1 = "This Is A   Test   String 1"

    characters = list(str_1)
    print(f"characters = {characters}")
    characters.reverse()
    print(f"characters = {characters}")
    print(f"reversed string = {''.join(characters)}")


# function_2()


def function_3():
    list_1 = ['t', 'h', 'i', 's']

    print(f"string 1 = {''.join(list_1)}")
    print(f"string 1 = {''.join(list_1)}")
    print(f"string 1 = {'-'.join(list_1)}")
    print(f"string 1 = {'*-*'.join(list_1)}")


# function_3()


def function_4():
    str_1 = "   test string     "

    print(f"str_1 = {str_1}")
    print(f"left trimmed str_1 = {str_1.lstrip()}")
    print(f"right trimmed str_1 = {str_1.rstrip()}")
    print(f"trimmed str_1 from both the ends = {str_1.strip()}")


# function_4()

def function_5():
    # string: collection of characters
    str_1 = "This      Is   A Test String  1"
    characters = list(str_1)
    print(f"characters = {characters}")


# function_5()


def function_6():
    str_1 = "sunbeam"
    str_2 = "sunbeam institute"

    # f-string or formatted string
    # print(f"str_1 = {str_1}, str_2 = {str_2}")
    # print("str_1 = {str_1}, str_2 = {str_2}")

    print("str_1 = {0}, str_2 = {1}".format(str_1, str_2))

    # left aligned
    print("str_1 = [{0:<20}], str_2 = [{1:<20}]".format(str_1, str_2))

    # right aligned
    print("str_1 = [{0:>20}], str_2 = [{1:>20}]".format(str_1, str_2))

    # center aligned
    print("str_1 = [{0:^20}], str_2 = [{1:^20}]".format(str_1, str_2))


# function_6()


def function_7():
    number = 12

    # print positive symbol
    print("decimal number = {0:+}".format(number))

    # print negative symbol
    print("decimal number = {0:-}".format(number))

    # decimal
    print("decimal number = {0}".format(number))

    # decimal
    print("decimal number = {0:n}".format(number))

    # decimal
    print("decimal number = {0:d}".format(number))

    # binary
    print("binary number = {0:b}".format(number))

    # octal
    print("octal number = {0:o}".format(number))

    # lower hexadecimal
    print("hexadecimal number = {0:x}".format(number))

    # upper hexadecimal
    print("hexadecimal number = {0:X}".format(number))


# function_7()


def function_8():
    number = 1350.5234234

    print("number = {0}".format(number))

    # limit the decimal positions to 2
    print("number = {0:.2f}".format(number))

    # scientific format
    print("number = {0:e}".format(number))

    # scientific format
    print("number = {0:E}".format(number))


# function_8()


def function_9():
    str_1 = 'abc'
    str_2 = '20'

    print(f"isalpha   str_1 = {str_1.isalpha()}, str_2 = {str_2.isalpha()}")
    print(f"isnumeric str_1 = {str_1.isnumeric()}, str_2 = {str_2.isnumeric()}")
    print(f"islower   str_1 = {str_1.islower()}, str_2 = {str_2.islower()}")


# function_9()


def function_10():
    str_1 = 'abc'

    print(f"str_1 = {str_1}")
    print(f"str_1 = {str_1:>10}")
    print("str_1 = {0:>10}".format(str_1))


# function_10()


def function_11():
    string = "red,green,yellow,black,brown"

    colors = string.split(',')
    print(f"colors = {colors}")

    timestamp = "13-04-2021T09:05 am"
    timestamp_components = timestamp.split('T')
    print(f"components = {timestamp_components}")

    date = timestamp_components[0]
    date_components = date.split('-')
    print(f"date_components = {date_components}")

    time = timestamp_components[1]
    time_components = time.split(' ')
    print(f"time_components = {time_components}")
    hours_minutes = time_components[0].split(':')
    print(f"hours_minutes = {hours_minutes}")

    print(f"day: {date_components[0]}, month: {date_components[1]}, year: {date_components[2]}, hours: {hours_minutes[0]}, minutes: {hours_minutes[1]}, meridian: {time_components[1]}")


# function_11()


def function_12():
    str_1 = "this ^is a %test &string"
    print(f"str_1 = {str_1}")

    # replace % character
    str_1 = str_1.replace('%', '')
    print(f"str_1 = {str_1}")

    # replace & character
    str_1 = str_1.replace('&', '')
    print(f"str_1 = {str_1}")

    # replace ^ character
    str_1 = str_1.replace('^', '')
    print(f"str_1 = {str_1}")

    # replace 'test' with 'another'
    str_1 = str_1.replace('test', 'another')
    print(f"str_1 = {str_1}")


# function_12()