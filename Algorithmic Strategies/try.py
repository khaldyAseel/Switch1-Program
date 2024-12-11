def common_nums(arr1,arr2):
    nums = []
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if arr1[i] == arr2[j] and arr1[i] not in nums:
                nums.append(arr1[i])
    
    return nums

#print(common_nums([1,2,3],[2,4,5]))


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


def common_nums3(arr1,arr2,arr3):
    nums = common_nums2(arr1,arr2)

    return common_nums2(nums,arr3)

print(f"common nums between three arrays :{common_nums3([1,4,5,3],[2,3,6,7],[1,2,4,3])}")


