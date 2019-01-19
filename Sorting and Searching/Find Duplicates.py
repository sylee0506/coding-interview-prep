#cracking the coding interview 10.8 (p151)
#find all the elements that appear twice in this array, without extra space
#used value as index, time complexity O(n), space complexity O(1)

class Solution:
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        for x in nums:
            if nums[abs(x)-1] < 0:
                ans.append(abs(x))
            else:
                nums[abs(x)-1] *= -1
        return ans
