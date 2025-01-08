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
    allSet = set(lst1,lst2)
    if len(allSet)!= len(lst1):
        return False
    else:
        for i in range(len(lst1)):
            indx1[lst1[i]] = i
        for j in range(len(lst2)):
            indx2[lst2[j]] = j
        if indx1[lst1[0]] == indx2[lst2[0]]:
            return False
        return True