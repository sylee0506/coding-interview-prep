#cracking the coding interview 10.11 (p151)
#find peak element in array (nums[i] ≠ nums[i+1] / nums[-1] = nums[n] = -∞)
#used binary search : O(logn)

class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
            
        while True:
            if left == right:
                return left
            elif left+1 == right:
                if nums[left] < nums[right]:
                    return right
                else:
                    return left
                
            mid = (left + right) // 2
            
            if nums[mid-1]<nums[mid]>nums[mid+1]:
                return mid
            elif nums[mid-1]>nums[mid]:
                right = mid
            else:
                left = mid
