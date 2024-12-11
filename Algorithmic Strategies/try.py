# Common elements ecercise in o(n^2) 
def common_nums(arr1,arr2):
    nums = []
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if arr1[i] == arr2[j] and arr1[i] not in nums:
                nums.append(arr1[i])
    
    return nums

#print(common_nums([1,2,3],[2,4,5]))


# Common elements ex in 0(n) 
def common_nums2(arr1,arr2):
    nums = {}
    common_elements = []
    for num in arr1:
        nums[num] = nums.get(num, 0) + 1

    for num in arr2:
        if num in nums and nums[num] > 0:
            common_elements.append(num)
            nums[num] -= 1

    return common_elements

print(f"common nums between tow arrays:{common_nums2([1,2,3],[2,1,3])}")

# Common elements in 3 arrays ex
def common_nums3(arr1,arr2,arr3):
    nums = common_nums2(arr1,arr2)

    return common_nums2(nums,arr3)

print(f"common nums between three arrays :{common_nums3([1,4,5,3],[2,3,6,7],[1,2,4,3])}")


# 1.Count vowels
def count_vowels(str):
    vol = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for char in str:
        if char in vol:
            count+=1
    return count 
str = "computer"
print(f"count of vowels in {str} is {count_vowels(str)}")
print(f"count of constants in {str} is {len(str) - count_vowels(str)}")



# 2.Median char 
def median_char(str):

    res = ''.join(sort_str(str))
    if len(res)%2 == 0:
        median = int((len(res)-1)/2)
    else:
        median = int((len(res))/2)
    return res[median]

# QuickSort forsorting the string 
def sort_str(s):
    chars = list(s)
    if len(chars) <= 1:
        return chars
    else:
        pivot = chars[0]
        lesser = [c for c in chars[1:] if c <= pivot]
        greater = [c for c in chars[1:] if c > pivot]
        return sort_str(lesser) + [pivot] + sort_str(greater)

print(f"median char is:{median_char('question')}")


# 3.Word Score
def word_score(str):
    str = str.lower()
    