'''def sum(arr):
    if len(arr) == 1:
        return arr.pop(0)
    else:
        return arr.pop(0) + sum(arr)

print(sum([2,4,5,7,6,8,0]))'''
'''def rec_len(arr):
    if len(arr) == 0:
        return 0
    else:
        arr.pop()
        return  rec_len(arr) + 1
print(rec_len([1,3,2,5,6,8]))
print([33,12,42,52].sort())'''
def quicksort(arr):
    if len(arr)<2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)
print(quicksort([42,33,81,31,25]))