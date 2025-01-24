# to pick a num from sorted array 1-100 without reapeting the num with 0(1) complexity:
import random

def draw(numbers, remaining):
    """
    Draw a number randomly from the list without repetition.
    :param numbers: The list of numbers to draw from.
    :param remaining: The count of remaining active numbers in the list.
    :return: The drawn number.
    """
    if remaining == 0:
        raise ValueError("All numbers have been drawn.")
    
    # Pick a random index within the active range
    rand_index = random.randint(0, remaining - 1)
    
    # Swap the randomly selected number with the last active number
    drawn_number = numbers[rand_index]
    numbers[rand_index], numbers[remaining - 1] = numbers[remaining - 1], numbers[rand_index]
    
    # Reduce the count of active numbers
    remaining -= 1
    
    return drawn_number, remaining


# Initialize the list and active range
numbers = list(range(1, 101))  
remaining = len(numbers)      

for _ in range(5):  # Draw 5 numbers without repetition
    print(draw(numbers))

# Example: Draw numbers without repetition
print("\nDrawing numbers without repetition:")
while remaining > 0:
    drawn, remaining = draw(numbers, remaining)
    print(drawn)
