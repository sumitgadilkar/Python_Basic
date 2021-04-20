# function as a variables

def function_1():
    print(f'inside function')

function_1()
#Fucntion alias = funtion 2 calling function 1 body
function_2 = function_1
function_3 = function_1
print(f'function_1 = {function_1}')
print(f'function_2 = {function_2}')
print(f'function_3 = {function_3}')

# Return none as function_1 is returning NONE
function_4 = function_1()
print(f'function_4 = {function_4}')

