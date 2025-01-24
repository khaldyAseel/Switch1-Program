class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        indecis = []
        if len(nums) == 0:
            return None
        
        for i in range(len(nums)):
            tmp = target - nums[i]
            for j in range(i+1,len(nums)):
                if nums[j] == tmp and i!=j:
                    indecis.append(i)
                    indecis.append(j)
                    break
        
        return indecis

def three_sum_indices(nums, target):
    # Create a list of (value, index) pairs
    nums_with_indices = [(num, idx) for idx, num in enumerate(nums)]
    # Sort based on values
    nums_with_indices.sort(key=lambda x: x[0])
    
    # Iterate through the sorted array
    for i in range(len(nums_with_indices) - 2):
        # Fix the first number
        first_value, first_index = nums_with_indices[i]
        left = i + 1
        right = len(nums_with_indices) - 1
        
        # Use two pointers to find the other two numbers
        while left < right:
            second_value, second_index = nums_with_indices[left]
            third_value, third_index = nums_with_indices[right]
            current_sum = first_value + second_value + third_value
            
            if current_sum == target:
                # Return the original indices of the three numbers
                return [first_index, second_index, third_index]
            elif current_sum < target:
                left += 1  # Increase the sum
            else:
                right -= 1  # Decrease the sum
    
    # If no such triplet is found, return an empty list
    return []

# Example usage
nums = [1, 4, 5, 2, 3, 7]
target = 12
print(f"Indices of elements that sum to {target}:", three_sum_indices(nums, target))

