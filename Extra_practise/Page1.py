
def function_1():
    cars = [
        {"model": "x4", "price": 80000, "company": "BMW"},
        {"model": "Q2", "price": 90000, "company": "MERC"},
        {"model": "Wings", "price": 20000, "company": "Tesla"},
        {"model": "Swift", "price": 10000, "company": "BMW"},
    ]

    new_car = (lambda i: {
      "model" : i["model"], "company" : i["company"]})

    model_price = list(map(new_car,cars))

    print(model_price)


#function_1()



def function_2():
    # list of dictionaries
    persons = [
        {"name": "person1", "email": "p1@test.com", "address": "pune", "age": 10},
        {"name": "person2", "email": "p2@test.com", "address": "mumbai", "age": 18},
        {"name": "person3", "email": "p3@test.com", "address": "satara", "age": 50}
    ]

    # Name and address of person > = 18 age
    right_candidate =  lambda p : p["age"]>= 18
    new_list  = (list(map(right_candidate, persons)))
    print(new_list)

#function_2()

#list = [10,20,30,40,50,60]
#print(f"{list[::-1]}")

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]


#Zip
l2 = ('s',"u","m","i","t")
l3 = (1,2,3,4,5)
#result = list(zip(l2,l3))

#print(f"Zip results are: {result}")

#List comprehension
l = [1,2,3,4,5,6,7,8,]
l1 = [i for i in l if i % 2 == 0]
#print(f"Even numbers are: {l1}")

#ZIP function:

l = [2,3,4,5]
n = [4,6,16,25]

result = [j/i for i,j in zip(l,n)]
#print(f"{result}")

total_sales = [52000,51000,48000]
prod_cost = [46800, 45900, 43200]

#Cal total Profit from the above sales data:
for total, cost in zip(total_sales,prod_cost):
    profit = total - cost
    #print(f'Profit from this sales : {profit}')





aList = [1, 2, 3, 4, 5, 6, 7]

square = (list(map(lambda i: i**2, aList)))
print(f"Square of aList : {aList} is : {square}")