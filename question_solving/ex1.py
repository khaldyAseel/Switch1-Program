# Write a simple camelCase method for strings. All words (except for the first) must have their first letter capitalized without spaces.
# input : "camel is An animaL" -> "camelIsAnAnimal"

def return_camel_case(str):
    returned_str = ""
    for i in range(1,len(str)):
        if str[i-1] == " ":
            returned_str+= str[i].upper()
        elif str[i]!= " ":
            returned_str+=str[i].lower()
    if str[0]!= " ":
        returned_str = str[0]+returned_str
    
    return returned_str

str = "camel is An animaL"
print(f"camel case of input is: {return_camel_case(str)}")

