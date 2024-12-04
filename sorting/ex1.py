def binary_search(arr,value,low=None,high=None):
     
    if low is None or high is None:
        low = 0
        high = len(arr) - 1

    if high>=low:
        mid = low+(high -low) //2

        if arr[mid] == value:
            return mid
    
        elif value<arr[mid]:
            return binary_search(arr,value,low,mid-1)
        else:
            return binary_search(arr,value,mid+1,high)
    else: 
        return -1
    


print(binary_search([12,34,45,46,47],34))