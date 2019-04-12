#Given an unsorted integer array, find the smallest missing positive integer
#time complexity: O(n)(or O(nlog(n)) / space complexity: O(1)

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
    
        if len(nums) == 0 or nums[-1] < 1:
            return 1
    
        if len(nums) == 1:
            if nums[0] != 1:
                return 1
            else:
                return 2
        
        temp_index = -1
        for i in range(len(nums)):
            if nums[i] <= 0:
                temp_index = i
                continue
            if i == (temp_index + 1) and nums[i] > 1:
                return 1
            if i > (temp_index + 1) and nums[i] > nums[i-1] and nums[i] != nums[i-1] + 1:
                return nums[i-1]+1
    
        return nums[-1]+1
