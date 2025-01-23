# Sort 012 with quick sort 

def sort_array(arr,low=0,high=None):   
    if high is None:
        high = len(arr) - 1
        
    if low<high:
        pivot = high
        i = low -1
        for j in range(low,high):
            if arr[j] < arr[pivot]:
                i+=1
                arr[i], arr[j] = arr[j], arr[i]

        arr[pivot],arr[i+1] = arr[i+1] ,arr[pivot]
        pivot = i + 1 
        sort_array(arr, low, pivot - 1) 
        sort_array(arr, pivot + 1, high)
    return arr 

print(f"Quick sort with space o(1):{sort_array([2,1,1,0,2])}")