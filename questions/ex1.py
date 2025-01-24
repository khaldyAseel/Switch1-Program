# to pick a num from sorted array 1-100 without reapeting the num with 0(1) complexity:
import random

def draw(numbers):
    size = len(numbers)
    if len(numbers) == 0:
        raise ValueError("All numbers have been drawn.")
        
    # Pick a random index within the active range
    rand_index = random.randint(0, size - 1)
        
    # Swap the randomly selected number with the last number in the active range
    drawn_number = numbers[rand_index]
    numbers[rand_index],numbers[size - 1] = numbers[size - 1], numbers[rand_index]
        
    size -= 1
        
    return drawn_number


numbers = list(range(1, 101)) 
print(f"drawn numbers is: {draw(numbers)}")