# 1 - merge sort with O(1) space 
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
    
    

# 2 - Sort numbers – by absolute values
def merge_sort_abs(arr):
    
    if len(arr)>1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort_abs(left)
        merge_sort_abs(right)

        i = 0
        j = 0
        k = 0
        while i<len(left) and j<len(right):
            if abs(left[i])<=abs(right[j]):
                arr[k] = abs(left[i])
                i+=1
            else:
                arr[k] = abs(right[j])
                j+=1
            k+=1

        while i<len(left):
            arr[k] = abs(left[i])
            i+=1
            k+=1
        
        while j<len(right):
            arr[k] = abs(right[j])
            j+=1
            k+=1

    return arr
    

# 3 - Sort list of strings – capital before lowercase
def merge_sort_strings(arr):
    
    if len(arr)>1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort_strings(left)
        merge_sort_strings(right)

        i = 0
        j = 0
        k = 0
        while i<len(left) and j<len(right):
            if left[i].islower():
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

# 4 - Sort numbers – odd should be before even
def merge_sort_odd(arr):
    
    if len(arr)>1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort_odd(left)
        merge_sort_odd(right)

        i = 0
        j = 0
        k = 0
        while i<len(left) and j<len(right):
            if left[i]%2 == 1:
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
   
# 5 - Sort numbers – primes before the rest
def merge_sort_primes(arr):
    
    if len(arr)>1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort_primes(left)
        merge_sort_primes(right)

        i = 0
        j = 0
        k = 0
        while i<len(left) and j<len(right):
            if is_prime(left[i]):
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

def is_prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True



print(f"merge sort with o(1) complexity:{merge_sort([2,4,3,7,5])}")
print(f"merge sort with absolute values:{merge_sort_abs([-1,-5,4,3,7])}")
print(f"merge sort with strings:{merge_sort_strings(['a','A','b','C','d'])}")
print(f"merge sort first odd nums then even:{merge_sort_odd([3,6,4,12,8])}")
print(f"merge sort with prime numbers:{merge_sort_primes([2,6,8,5,3,7])}")
