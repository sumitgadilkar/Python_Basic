def function_1():

    dict_01 = {"India":91, "USA": 1, "Germany": 98}
    dict_02 = {"Australia" : 61,
               "Italy" : 31,
               "Germany" : 90
                                 }

    #merge two dictionaries
    dict_01.update(dict_02)
    print(dict_01)
    #print(dict_02)

function_1()