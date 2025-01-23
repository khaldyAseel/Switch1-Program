# Longest substring

def longest_substring(s):
    char_index = {}
    max_length = 0
    start = 0  # Start of the current window

    for end in range(len(s)):
        # If the character is already in the window, move the start pointer
        if s[end] in char_index and char_index[s[end]] >= start:
            start = char_index[s[end]] + 1
        
        # Update the character's index
        char_index[s[end]] = end

        # Update the maximum length
        max_length = max(max_length, end - start + 1)

    return max_length


# Example Usage
print(f"longest substring is: {longest_substring("abcda")}")
