# Acoording to the design principles KISS(keep it simple) 
# we can write claculate_avarge function in a more simple way 

def calculate_average(numbers):
    """
    Calculate the average of a list of numbers.
    """
    average = sum(numbers) / len(numbers)
    return round(average, 2)


# Usage
try:
    result = calculate_average([1, 2, 3, 4, 5])
    print(f"The average is: {result}")
except (TypeError, ValueError) as e:
    print(f"Error: {str(e)}")

# Acoording to the design principles KISS(keep it simple) we can write claculate_avarge function in a more simple way 



