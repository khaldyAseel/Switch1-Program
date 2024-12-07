#1.bubble sort with space complexity o(1)
def bubble_sort(arr):
    n = len(arr) 
    for i in range(n-1): 
        for j in range(0, n-i-1): 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 
    return arr

arr = [64, 34, 25, 12, 22, 11, 90] 
print(f"Sorted array: {bubble_sort(arr)}")


#2.bubble sort by diff from target 
def bubble_sort_by_target(arr, target):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            # Compare absolute difference with the target
            if abs(arr[j] - target) > abs(arr[j + 1] - target):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Example
arr = [10, 2, 8, 3, 5]
target = 5
sorted_arr = bubble_sort_by_target(arr, target)
print(f"Sorted array based on distance from {target}: {sorted_arr}")

# 3. bubble sort by palindromic numbers first
def bubble_sort_by_palindrome(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            # If the current number is not palindromic but the next one is, swap them
            if not is_palindrome(arr[j]) and is_palindrome(arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            # If both are palindromic or non-palindromic, sort normally
            elif (is_palindrome(arr[j]) == is_palindrome(arr[j + 1]) 
                  and arr[j] > arr[j+1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def is_palindrome(num):
    """Check if a number is a palindrome."""
    str_num = str(num)
    return str_num == str_num[::-1]

# Example
arr = [121, 34, 22, 11, 90, 101, 454]
sorted_arr = bubble_sort_by_palindrome(arr)
print(f"Sorted array prioritizing palindromic numbers: {sorted_arr}")

