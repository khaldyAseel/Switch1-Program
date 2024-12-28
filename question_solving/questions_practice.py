# Given an array, find the int that appears an odd number of times.
def odd_int(arr): #[1,2,3,2,1]
    occ = {}

    for i in range(len(arr)):
        if arr[i] in occ:
            occ[arr[i]]+=1
        else:
            occ[arr[i]] = 1

    for num in arr:
        if occ[num]%2 == 1:
            return num
        else:
            return None

print(f"the first num that appear in a odd numbers is: {odd_int([1,2,3,2,1])}") 


# Find in a sorted array the closest number to a given number
def closest_num(arr,num):  #[1,2,4,5] , num=6 to return 5 
    min_diff = arr[0]

    for i in range(len(arr)):
        diff = abs(arr[i] - num)
        if diff < min_diff:
            min_diff = diff
            

    return num - min_diff

print(closest_num([1,2,4,5],6))