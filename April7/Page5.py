

# Lambda as per class: need not add complex function in lambda exp

subtract =  lambda p1,p2 : p1 - p2
print(f'{subtract(4,6)}')


def add(p3, p4):
    return p3 + p4

addition = lambda x,y : add(x,y)
print(f'Addition of two numbers : {addition(6,7)}')




