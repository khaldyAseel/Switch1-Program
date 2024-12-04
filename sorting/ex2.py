# 1 - merge sort with O(1) space 
def merge_sort(arr):
    
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        print(left)
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)

    i = len(arr)-1
    print(i)
    while i>=0:
        if left and right:
            if left[i]>=right[i]:
                arr[i] = left.pop()
            else:
                arr[i] = right.pop()
        else:
            arr[i] = left.pop() if left else right.pop()
        i -=1

    return arr    
    
    

# 2 - Sort numbers – by absolute values
def merge_sort_abs(arr):
    
    if len(arr)>1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort_abs(left)
        merge_sort_abs(right)

    i = len(arr)-1
    while i>=0:
        if len(left)>=1 and len(right)>=1:
            if abs(left[i])>=abs(right[i]):
                arr[i] = abs(left.pop())
            else:
                arr[i] = abs(right.pop())
        else:
            arr[i] = abs(left.pop()) if len(left) ==1 else abs(right.pop())
        i -=1

        return arr  
    

# 3 - Sort list of strings – capital before lowercase
def merge_sort_strings(arr):
    
    if len(arr)>1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort_strings(left)
        merge_sort_strings(right)

    i = len(arr)-1
    while i>=0:
        if len(left)>=1 and len(right)>=1:
            if left[i].islower():
                arr[i] = left.pop()
            else:
                arr[i] = right.pop()
        else:
            arr[i] = left.pop() if len(left) ==1 else right.pop()
        i -=1

        return arr

# 4 - Sort numbers – odd should be before even
def merge_sort_odd(arr):
    
    if len(arr)>1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort_odd(left)
        merge_sort_odd(right)

    i = len(arr)-1
    while i>=0:
        if len(left)>=1 and len(right)>=1:
            if left[i] % 2 == 1:
                arr[i] = left.pop()
            else:
                arr[i] = right.pop()
        else:
            arr[i] = left.pop() if len(left) ==1 else right.pop()
        i -=1

        return arr  
   
# 5 - Sort numbers – primes before the rest
def merge_sort_primes(arr):
    
    if len(arr)>1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort_primes(left)
        merge_sort_primes(right)

    i = len(arr)-1
    while i>=0:
        if len(left)>=1 and len(right)>=1:
            if left[i].is_prime():
                arr[i] = left.pop()
            else:
                arr[i] = right.pop()
        else:
            arr[i] = left.pop() if len(left) ==1 else right.pop()
        i -=1

        return arr 

def is_prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True



print(merge_sort([2,4,3,7,5]))
