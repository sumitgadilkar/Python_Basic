def function_1():
    str_1 = "this &is &a &test &string"
    print(f"str_1 = {str_1}")

    # str_1 = str_1.replace('&', '')
    # print(f"str_1 = {str_1}")

    list_1 = list(str_1)
    position = list_1.index('&')
    list_1.pop(position)
    str_1 = ''.join(list_1)
    print(f"str_1 = {str_1}")


# function_1()


def function_2():
    filename = "myfile.jpg"
    parts = filename.split('.')
    print(f"file name = {parts[0]}")
    print(f"extension = {parts[1]}")


# function_2()


def function_3():
    string = "this $is ^a &&test @string 1. this is a ~@^test string 2. this is a test string 3."

    print(f"is 'my' word present in the string = {'my' in string}")
    print(f"is 'this' word present in the string = {'this' in string}")

    unwanted_characters = '~!@#$%^&*()'

    final_string = []
    for character in string:
        # print(f"character = {character}")

        # check if the character is a special character
        # if the character is special then do not consider the character
        if character not in unwanted_characters:
            final_string.append(character)

    print(f"string = {string}")
    print(f"final_string = {final_string}")
    print(f"final_string = {''.join(final_string)}")


# function_3()

def function_4():
    string = "this $is ^a &&test @string 1. this is a ~@^test string 2. this is a test string 3."
    unwanted_characters = '~!@#$%^&*()'

    print(f"string = {string}")

    for character in unwanted_characters:
        string = string.replace(character, '')

    print(f"string = {string}")


function_4()