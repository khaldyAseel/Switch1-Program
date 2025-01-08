# A mistake can be:
# missing letter – abc, ba
# 1 replacement – abc,  cna

def missing_ch(word1,word2):
    charCounter = {}
    for ch in word1:
        if charCounter.__contains__(ch):
              charCounter[ch] +=1
        charCounter[ch] = 1
    for ch in word2:
        if charCounter.__contains__(ch):
              charCounter[ch] +=1
        charCounter[ch] = 1
    print(charCounter)
    for letter in charCounter: 
        if charCounter[letter] == 1:
            return True
        return False
        

print(missing_ch('abc','ba'))
print(missing_ch('abc','cna'))
print(missing_ch('abc','abc'))

