#find the missing number of an array 1-100
def missing_num(arr):
    lst = list(range(1, 11))
    sum1 = sum(arr)
    sum2 = sum(lst)
    return sum2 - sum1

print(missing_num([1,2,3,5,6,7,8,9,10]))