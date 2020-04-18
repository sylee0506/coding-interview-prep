#Find all the elements of [1,n] inclusive that do not appear in given array
#time complexity: O(n)
#without extra space (returned answer is not regarded as extra space)

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = {i for i in range(1, len(nums)+1)}
        
        ans = ans - set(nums)
                
        return ans


#other solution not using set
'''
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # For each number i in nums,
        # we mark the number that i points as negative.
        # Then we filter the list, get all the indexes
        # who points to a positive number
        for i in xrange(len(nums)):
            index = abs(nums[i]) - 1
            nums[index] = - abs(nums[index])

        return [i + 1 for i in range(len(nums)) if nums[i] > 0]
'''
#same algorithm, but more pythonic
'''
def findDisappearedNumbers(self, nums):
    for num in nums:
        index = abs(num) - 1
        nums[index] = -abs(nums[index])
            
    return [i + 1 for i, num in enumerate(nums) if num > 0]
'''
