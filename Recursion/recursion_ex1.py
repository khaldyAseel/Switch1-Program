
# recursion fibonacci
def fibonacci(size):
    if size <=1:
        return size 
  
    return fibonacci(size -1) + fibonacci(size -2)

print(fibonacci(6))