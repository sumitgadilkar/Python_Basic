def merge(left,right):
    result = []
    i,j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i+= 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]
    return result



def merge_sort(lst):
    if len(lst) <= 1:
        return lst

    mid = len(lst)//2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])

    return merge(left,right)



arr = [89,54,3,43,11,-1, 65,4]
print(merge_sort(arr))



