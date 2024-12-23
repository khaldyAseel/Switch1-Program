# Write a simple camelCase method for strings. All words (except for the first) must have their first letter capitalized without spaces.

# input : "camel is An animaL" -> "camelIsAnAnimal"
# iterate over string 

#def return_camel_case(str):
#    returned_str = " "

#    for i in range(0,len(str)-1):
#        if str[i]!= " ":
            

# to return second buggest number in given array 

def second_biggest_num(arr):
     arr = sorted(arr)
     length = len(arr)
     return arr[length-2]  

# test 1:
print (f"second biggest num is: {second_biggest_num([2,3,5,7,4])}")
# test 2:
print (f"second biggest num is: {second_biggest_num([2,3,5,-7,4])}")

def second_biggest_num1(arr):
    sorted_arr = merge_sort(arr)
    length = len(sorted_arr)
    return arr[length-2]

def merge_sort(arr):
    
    if len(arr)>1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = 0
        j = 0
        k = 0
        while i<len(left) and j<len(right):
            if left[i]<=right[j]:
                arr[k] = left[i]
                i+=1
            else:
                arr[k] = right[j]
                j+=1
            k+=1

        while i<len(left):
            arr[k] = left[i]
            i+=1
            k+=1
        
        while j<len(right):
            arr[k] = right[j]
            j+=1
            k+=1

    return arr  

# test 1:
print (f"second biggest num with merge sort is: {second_biggest_num1([0,21,4,6])}")
# test 2:
print (f"second biggest num with merge sort is: {second_biggest_num1([2,3,5,-7,4])}")