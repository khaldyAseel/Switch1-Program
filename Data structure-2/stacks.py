class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    def is_empty(self):
        return len(self.stack) == 0


def is_valid(string):
    # Dictionary to map opening to closing brackets
    bracket_map = {"(": ")", "[": "]", "{": "}"}
    stack = Stack()
    
    for char in string:
        if char in bracket_map:  # If it's an opening bracket
            stack.push(char)
        else:  # If it's a closing bracket
            if stack.is_empty():  # If the stack is empty, it's invalid
                return False
            top = stack.pop()
            if bracket_map[top] != char:  
                return False
    
    return stack.is_empty()  # Return True if no unmatched opening brackets remain


print(is_valid("[()]{}"))  # True
print(is_valid("{[()]}"))  # True
print(is_valid("[({})]"))  # True
print(is_valid("[({)}]"))  # False
print(is_valid("{[("))     # False
print(is_valid("]}"))      # False
