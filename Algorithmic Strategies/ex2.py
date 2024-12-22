#Chars to Lengths   
#We want to count for each letter how many times it repeats one after the other. 
#For a string aaabbcb, it will print output a3b2c1b1

def get_chars_dup(str):
    counts = []
    count = 1
    j = 0
    for i in range(1,len(str)):
        if str[i] == str[i-1]:
            count+=1
    else:
        counts.append(count)
        count = 1
    for count in counts:
        word = str[j] + str(count)
        j+=1 
    return word 

print(get_chars_dup('aaabbcb'))



def get_chars_dup(s):
    counts = []
    result = ""
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            counts.append((s[i-1], count))
            count = 1  
    
    counts.append((s[-1], count))
    
    for char, count in counts:
        result += char + str(count)
    
    return result

