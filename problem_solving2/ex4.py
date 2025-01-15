# Examples:
# "listen" → "silent"
# "earth" → "heart"

# word split to char array 
# hashset to 2 words 
# hashset equal to char array? 
# list that i can save the indexes of the chars

def check_anagram(word1,word2):
    lst1 = list(word1)
    lst2 = list(word2)
    indx1 = {}
    indx2 = {}
    allSet = set(lst1 + lst2)
    if len(allSet)!= len(lst1):
        return False
    for i in range(len(lst1)):
        indx1[lst1[i]] = i
    for j in range(len(lst2)):
        indx2[lst2[j]] = j
    for key in indx1:
        if indx2.__contains__(key):
            return True
        else:
            return False

str1 = 'listen'
str2 = 'silent'
print(f"Is it anagram? {check_anagram(str1,str2)}")