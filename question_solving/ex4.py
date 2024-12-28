# Max repeating char
# Return the first max repeating Char in a string. Example: abafbch => a
def return_max_char(str):
    char_count = {}
    char_order = []

    for char in str:
        if char not in char_count:
            char_count[char] = 1
            char_order.append(char)
        else:
            char_count[char] += 1

    max_count = 0
    max_char = None
    for char in char_order: 
        if char_count[char] > max_count:
            max_count = char_count[char]
            max_char = char
    return max_char

print(f"The first max reparing char is: {return_max_char("abafbch")}")

