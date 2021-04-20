#parameterised function

def function_2(name, age=80 ):
    print("inside function1")
    print(f'name = {name}, type = {type(name)}')
    print(f'age = {age}')

function_2(age = 78, name = 'sumit')