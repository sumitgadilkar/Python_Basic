def bubble(l):

    for i in range (0, len(l)-1):
        print("value of i in first for loop", i, "value is", l[i])
        #print(f'(Value of j : {j}')
        for j in range(len(l)-1):
            print("value of i in second for loop ", i, "value is", l[i])
            print("value of j is ", j, "value of j :", l[j])
            print("value of j+1 is ", j+1, "value of j+1 :", l[j+1])
            # In loop:
            if l[j] > l[j+1]:
                print("In IF Loop")
                print("value of i in IF loop ", i, "value is", l[i])
                print("value of j is ", j, "value of j :", l[j])
                print("value of j+1 is ", j + 1, "value of j+1 :", l[j + 1])
                temp = l[j]
                l[j] = l[j+1]
                l[j+1] = temp
                print("After swapping values in IF loop")
                print("value of i is ", i, "value is", l[i])
                print("value of temp is", temp)
                print("value of j is ", j, "value of j :", l[j])
                print("value of j+1 is ", j + 1, "value of j+1 :", l[j + 1])
    return l

l = [99,56,78,45,9]

print(f'Sorted list is {bubble(l)}')


