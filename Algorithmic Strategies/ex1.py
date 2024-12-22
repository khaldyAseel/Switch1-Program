#Return the first non-repeating char in a string.
def get_non_repeating_char(str):
    chars = set(str)
    counts = {}

    for c in chars:
        counts[c] = 0

    for letter in str:
        counts[letter]+=1

    for index in counts:
        if counts[index]<2:
            return index
        

print(get_non_repeating_char('abcbcad'))

    