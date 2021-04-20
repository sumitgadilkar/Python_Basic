def selection_sort(x):

    for i in range(len(x)):
        min_val = i

        for j in range(i+1, len(x)):
            if x[j] < x[min_val]:
                min_val = j

        temp = x[i]
        x[i] = x[min_val]
        x[min_val] = temp

        print(f'After sorting: {x}')



s = [56,23,90,3,1,43,67,789,544,231,7,8,4,9,567,0]
selection_sort(s)