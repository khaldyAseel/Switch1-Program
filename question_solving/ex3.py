
# return true if str1 is rotation for str2 else false
def is_rotation(str1,str2):
    merged = str1 + str2
    if len(str1) == 0 and len(str2) == 0:
        return True
    if len(str1) != len(str2):
        return False
    if str2 in merged:
        return True  

str1 = 'abcd'
str2 = 'cdab'
#print(f"{str2} is rotation for {str1} :{is_rotation('abc','cba')}")


def check_rotation(str1,str2):
    if len(str1) != len(str2):
        return False
    for i in range(len(str1)):
        shifted = str1[i:] + str1[:i]
        if str2 == shifted:
            return True 
    return False 

str1 = 'abcd'  
str2 = 'cdab'   
print(f"{str2} is rotation for {str1} :{check_rotation(str1,str2)}")


