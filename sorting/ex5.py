# 1.heap sort with space complexity o(1)
def heapify(arr, n, i):
    largest = i  # Initialize the largest as root
    left = 2 * i + 1  # Left child index
    right = 2 * i + 2  # Right child index

    # If the left child is larger than the root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # If the right child is larger than the largest so far
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If the largest is not the root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        # Recursively heapify the affected subtree
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    # Step 1: Build a max-heap from the input array
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Step 2: Extract elements one by one
    for i in range(n - 1, 0, -1):
        # Move the current root (maximum) to the end
        arr[i], arr[0] = arr[0], arr[i]

        # Call heapify on the reduced heap
        heapify(arr, i, 0)

    return arr


# Example Usage
arr = [12, 11, 13, 5, 6, 7]
sorted_arr = heap_sort(arr)
print("Sorted array by heap sort:", sorted_arr)


#2. heap sort by value of the sum of the digits
def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

def heapify_2(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # Compare based on the sum of digits
    if left < n and sum_of_digits(arr[left]) > sum_of_digits(arr[largest]):
        largest = left
    elif left < n and sum_of_digits(arr[left]) == sum_of_digits(arr[largest]):
        if arr[left] > arr[largest]:
            largest = left

    if right < n and sum_of_digits(arr[right]) > sum_of_digits(arr[largest]):
        largest = right
    elif right < n and sum_of_digits(arr[right]) == sum_of_digits(arr[largest]):
        if arr[right] > arr[largest]:
            largest = right

    # If the largest is not the root, swap and heapify the affected subtree
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify_2(arr, n, largest)

def heap_sort_digits(arr):
    n = len(arr)

    # Build the heap (rearrange the array)
    for i in range(n // 2 - 1, -1, -1):
        heapify_2(arr, n, i)

    # One by one extract elements from the heap
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap
        heapify_2(arr, i, 0)

# Example usage:
arr = [24, 31, 12, 45, 33, 22, 5]
heap_sort_digits(arr)
print("Sorted array by value of the sum of the digits:", arr)


#3.heap sort by perfect numbers first 
#Function to check if a number is perfect
def is_perfect(n):
    if n < 2:
        return False
    divisors_sum = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors_sum += i
            if i != n // i:
                divisors_sum += n // i
    return divisors_sum == n

def heapify_3(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # Priority for perfect numbers
    if left < n and (is_perfect(arr[left]) and not is_perfect(arr[largest])):
        largest = left
    elif left < n and is_perfect(arr[left]) == is_perfect(arr[largest]):
        if arr[left] > arr[largest]:
            largest = left

    if right < n and (is_perfect(arr[right]) and not is_perfect(arr[largest])):
        largest = right
    elif right < n and is_perfect(arr[right]) == is_perfect(arr[largest]):
        if arr[right] > arr[largest]:
            largest = right

    # If the largest is not the root, swap and heapify the affected subtree
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify_3(arr, n, largest)

def heap_sort_perfectNum(arr):
   # Separate perfect and non-perfect numbers
    perfect_numbers = [num for num in arr if is_perfect(num)]
    non_perfect_numbers = [num for num in arr if not is_perfect(num)]

    # Sort the non-perfect numbers
    n = len(non_perfect_numbers)
    for i in range(n // 2 - 1, -1, -1):
        heapify(non_perfect_numbers, n, i)

    # Sort the perfect numbers
    n = len(perfect_numbers)
    for i in range(n // 2 - 1, -1, -1):
        heapify(perfect_numbers, n, i)

    # Concatenate the sorted perfect and non-perfect numbers
    arr[:] = perfect_numbers + non_perfect_numbers

# Example usage
arr = [6, 28, 496, 12, 33, 8, 5]
heap_sort_perfectNum(arr)
print("Sorted array by the perfect numbers first:", arr)
