#Permutations of a String
#Problem: Write a function to generate all possible permutations of a given string.
#Example Input: permutations("abc")
#Expected Output: ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

def permutations(word,perfix=""):
    words = []
    if word is None:
        return []
    if len(word) == 0:
        words.append(perfix)
    else:
        for i in range(len(word)):
            next_perfix = perfix + word[i]
            remaining = word[i+1:] + word[:i]
            words.extend((permutations(remaining,next_perfix)))

    return words    
    
        
print(permutations('abc'))


#Problem:  
#You are given an n×n matrix of integers. A "magic box" is a 3x3 submatrix within this larger matrix where all the elements are distinct. 
#Your task is to write a function that identifies how many such 3x3 magic boxes exist in the matrix.
import random 

def magic_box(matrix):
    nums = set()
    matrix2 = []
    if len(matrix) < 3 or len(matrix[0]) < 3:
        return False
    temp1 = random.randint(0,len(matrix)-3)
    temp2 = random.randint(0, len(matrix[0]) - 3)
    print(temp1)
    for i in range(temp1,temp1+3):
        for j in range(temp2,temp2+3):
            if matrix[i][j] in nums:
                return False
            nums.add(matrix[i][j])
            matrix2.append(matrix[i][j])

    print(f"Submatrix: {matrix2}")
    return True

print(magic_box([[1,2,3,4],
                [2,5,6,7],
                [8,9,10,11]]))