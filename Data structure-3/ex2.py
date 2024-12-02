#Permutations of a String
#Problem: Write a function to generate all possible permutations of a given string.
#Example Input: permutations("abc")
#Expected Output: ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

def permutations(word):
    words = []
    if word is None:
        return []
    if len(word) == 1:
        return words.append(word)
    for i in range(len(word)):
        lst = (permutations(word[i:]))
    
        

print(permutations('abc'))


#Problem:  
#You are given an n×n matrix of integers. A "magic box" is a 3x3 submatrix within this larger matrix where all the elements are distinct. 
#Your task is to write a function that identifies how many such 3x3 magic boxes exist in the matrix.