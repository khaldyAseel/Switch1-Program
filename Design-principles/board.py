# According to the design Principle Generic 
# we want to make our code generic 
import random

def initialize_board(row,col,val):
    numbers = list(range(1, val + 1))
    random.shuffle(numbers)
    board = []
    
    for i in range(row):
        board.append(numbers[i * row:(i + 1) * col])
    
    return board

# Example usage
board = initialize_board(5,5,100)
for row in board:
    print(row)
