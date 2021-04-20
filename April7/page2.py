# scope : global

num = 10
print(f'global variable {num}')
print(f'{num}')

def function_1():
    num = "sumit"

    print(f'name = {num}')

function_1()
print(f'num = {num}')


# modify value of global variable
def function_2():
    #global name is req only when global variables value needs to be altered
    global num
    num = 100
    num = 400
    print(f'global value = {num}')

function_2()
print(f'global variables value outside function_2 = {num}')
#global num is changed here as shown
num = 600

print(f'global value is again changed = {num}')

#Global value is changed here forever
#Global value can also be changed again outside of function
# Function variables are always local to a function


# Function as a variable
print(f'{function_2}, type ={type(function_2)}')

print("This is new statement")

print("This is statement3")
print("This is new statement4")
