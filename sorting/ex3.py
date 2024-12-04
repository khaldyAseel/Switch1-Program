# 1 - quick sort with  O(1) sapce complexity 
def quick_sort(arr,low=0,high=None):   
    if high is None:
        high = len(arr) - 1
        
    if low<high:
        pivot = high
        i = low -1
        for j in range(low,high):
            if arr[j] < arr[pivot]:
                i+=1
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp

        temp1 = arr[pivot]
        arr[pivot] = arr[i+1]
        arr[i+1] = temp1
        pivot = i + 1 
        quick_sort(arr, low, pivot - 1) 
        quick_sort(arr, pivot + 1, high)
    return arr 

print(f"Quick sort with space o(1):{quick_sort([45,25,3,4,6])}")

# 2 - fizz buzz quick sort 
def quick_sort_fizzbuzz(arr,low=0,high=None):   
    if high is None:
        high = len(arr) - 1
        
    if low<high:
        pivot = high
        i = low -1
        for j in range(low,high):
            if fizzbuzz_priority(arr[j]) < fizzbuzz_priority(arr[pivot]):
                i+=1
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp

        temp1 = arr[pivot]
        arr[pivot] = arr[i+1]
        arr[i+1] = temp1
        pivot = i + 1 
        quick_sort_fizzbuzz(arr, low, pivot - 1) 
        quick_sort_fizzbuzz(arr, pivot + 1, high)
    return arr 

def fizzbuzz_priority(num):
    if num % 3 == 0 and num % 5 == 0:
        return 1  
    elif num % 5 == 0:
        return 2  
    elif num % 3 == 0:
        return 3 
    else:
        return 4  

print(f"Quick sort with fizz buzz :{quick_sort_fizzbuzz([30,25,3,15,6])}")

def quick_sort_digits(arr,low=0,high=None):   
    if high is None:
        high = len(arr) - 1
        
    if low<high:
        pivot = high
        i = low -1
        for j in range(low,high):
            if count_digits(arr[j])<count_digits(arr[pivot]):
                i+=1
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp

        temp1 = arr[pivot]
        arr[pivot] = arr[i+1]
        arr[i+1] = temp1
        pivot = i + 1 
        quick_sort_digits(arr, low, pivot - 1) 
        quick_sort_digits(arr, pivot + 1, high)
    return arr 

def count_digits(num):
    count = 0
    while num != 0:
        num //= 10
        count += 1
    return count

print(f"Quick sort with num of digits :{quick_sort_digits([25,200,3,5,222])}")


def quick_sort_dev(arr,low=0,high=None):   
    if high is None:
        high = len(arr) - 1
        
    if low<high:
        pivot = high
        i = low -1
        for j in range(low,high):
            if num_deviation(arr[j])<num_deviation(arr[pivot]):
                i+=1
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp

        temp1 = arr[pivot]
        arr[pivot] = arr[i+1]
        arr[i+1] = temp1
        pivot = i + 1 
        quick_sort_dev(arr, low, pivot - 1) 
        quick_sort_dev(arr, pivot + 1, high)
    return arr

def num_deviation(num):
    # n= 3 
    return num% 3 

print(f"Quick sort with num of digits :{quick_sort_dev([12,11,3,5,18])}")
