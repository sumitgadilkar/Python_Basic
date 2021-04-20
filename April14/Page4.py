def function_1():
    # list of dictionaries
    persons = [
        {"name": "person1", "email": "p1@test.com", "address": "pune", "age": 10},
        {"name": "person2", "email": "p2@test.com", "address": "mumbai", "age": 18},
        {"name": "person3", "email": "p3@test.com", "address": "satara", "age": 50}
    ]

    # find the persons who are eligible for voting
    new_persons = []
    for person in persons:
        # check if person is eligible for voting
        if person['age'] >= 18:
            new_persons.append(person)

    print(f"new_persons = {new_persons}")


# function_1()

def function_2():
    # list of dictionaries
    persons = [
        {"name": "person1", "email": "p1@test.com", "address": "pune", "age": 10},
        {"name": "person2", "email": "p2@test.com", "address": "mumbai", "age": 18},
        {"name": "person3", "email": "p3@test.com", "address": "satara", "age": 50}
    ]

    is_eligible = lambda person: person['age'] >= 18
    new_persons = list(filter(is_eligible, persons))
    print(f"new_persons = {new_persons}")


# function_2()


def function_3():
    cars = [
        {"model": "i20", "company": "hyundai", "price": 7.5},
        {"model": "i10", "company": "hyundai", "price": 5.5},
        {"model": "fabia", "company": "skoda", "price": 6.5},
        {"model": "nano", "company": "tata", "price": 2.5},
        {"model": "X5", "company": "BMW", "price": 42},
        {"model": "discovery", "company": "range rover", "price": 96}
    ]

    # find affordable cars
    # criteria, price <= 10
    affordable_cars = list(filter(lambda car: car['price'] <= 10, cars))
    print(f"affordable cars = {affordable_cars}")


function_3()


def function_4():
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


#function_4()



def function_5():
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

#function_5()
