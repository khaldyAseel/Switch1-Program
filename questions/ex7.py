class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        size = len(nums1)+len(nums2)
        combined_nums = [0]*size
        ptr = 0
        j = 0 
        for i in range(0,len(combined_nums)): 
            if nums1[j]>nums2[ptr]:
                combined_nums[i] = nums2[ptr]
                combined_nums[i+1] = nums1[j]
                ptr+=1
                j+=1
                i+=1
            else:       
                combined_nums[i] = nums1[j]
        
        print(combined_nums)
        if len(combined_nums)%2 == 0:
            return combined_nums[len(combined_nums)/2]+combined_nums[len(combined_nums)/2 - 1]
        else: 
            return combined_nums[int(len(combined_nums)/2)]
        

Solution = Solution()
print(Solution.findMedianSortedArrays([1,2],[3]))