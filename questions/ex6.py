# max_sum of array first element is positive 

def max_sum(nums):
    max_sum = 0 
    if len(nums)==0 or nums[0]<=0:
        return 0
    for i in range(len(nums)):
        if(nums[i]>0):
            max_sum+=nums[i]
          
    return max_sum