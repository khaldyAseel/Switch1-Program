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

print(quick_sort([45,25,3,4,6]))

# 2 - fizz buzz quick sort 
def quick_sort_fizzbuzz(arr,low=0,high=None):   
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



print(quick_sort([45,25,3,4,6]))