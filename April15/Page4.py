#File Management

def function_1():
    # step 1: open the required file
    # w: write
    # r: read
    # a: append
    file = open('myfile.txt', 'w')

    # step 2: perform the operation

    # step 3: close the file
    file.close()


# function_1()


def function_2():
    file = open('myfile.txt', 'w')
    file.write("this is my first file")
    file.close()


# function_2()


def function_3():
    file = open('myfile.txt', 'r')

    # read all the contents in the file
    # data = file.read()

    print(f"file pointer is pointing to {file.tell()}")

    # read first 4 bytes
    data = file.read(4)
    print(f"data = {data}")
    print(f"file pointer is pointing to {file.tell()}")

    # read next 4 bytes
    data = file.read(4)
    print(f"data = {data}")
    print(f"file pointer is pointing to {file.tell()}")

    # read next 4 bytes
    data = file.read(4)
    print(f"data = {data}")
    print(f"file pointer is pointing to {file.tell()}")

    # set the file pointer location
    file.seek(0)
    print(f"file pointer is pointing to {file.tell()}")

    # read next 4 bytes
    data = file.read(4)
    print(f"data = {data}")
    print(f"file pointer is pointing to {file.tell()}")

    file.close()


# function_3()


def function_4():
    file = open('myfile.txt', 'r')

    # print(file.readline())
    # print(file.readline())
    # print(file.readline())
    # print(file.readline())

    lines = file.readlines()
    print(lines)

    for line in lines:
        print(line.replace('\n', ''))

    file.close()


# function_4()


def function_5():
    file = open('myfile.txt', 'a')
    file.write("\nthis is fifth line")
    file.close()


function_5()