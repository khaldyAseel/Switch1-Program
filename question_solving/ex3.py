
# return true if str1 is rotation for str2 else false
def is_rotation(str1,str2):
    str3 = str1 + str1
    if len(str1) == 0 or len(str2) == 0:
        return False
    if len(str1) == 0 and len(str2) == 0:
        return True
    if len(str1) != len(str2):
        return False
    if str2 in str3:
        return True  

str1 = 'abcd'
str2 = 'cdab'
print(f"{str2} is rotation for {str1} :{is_rotation('abc','cba')}")