def function_1():
    try:
        # used to add the code which may generate an error
        file = open("./test.txt", "r")
    except FileNotFoundError:
        # used to handle FileNotFoundError
        print("file not present on the location")

        # try:
        #     division = 10 / 0
        #     print(f"division = {division}")
        # except ZeroDivisionError:
        #     print("denominator can not be zero")

    except:
        # used to handle any other error than FileNotFoundError
        print("exception has received...")

        # try:
        #     division = 10 / 0
        #     print(f"division = {division}")
        # except ZeroDivisionError:
        #     print("denominator can not be zero")

    else:
        # used to add code which will be called only when
        # there is no exception being raised
        data = file.read()
        print(f"data = {data}")

        try:
            division = 10 / 0
            print(f"division = {division}")
        except ZeroDivisionError:
            print("denominator can not be zero")
        finally:
            print("finally called for division error")

    finally:
        # used to add the code which will be called
        # irrespective of error being raised
        if file != None:
            file.close()
        print("finally block called")

        # try:
        #     division = 10 / 0
        #     print(f"division = {division}")
        # except ZeroDivisionError:
        #     print("denominator can not be zero")


function_1()