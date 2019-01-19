#cracking the coding interview 10.3 (p150)
#suppose an array sorted in ascending order is rotated at some pivot, find target
#used binary search (o(logn))

class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        first = 0; last = len(nums)-1
        if nums == []:
            return -1
        
        while first <= last:
            if first == last:
                if target == nums[first]:
                    return first
                else:
                    return -1
                
            mid = (first+last)//2
            
            if target > nums[mid]:
                if target > nums[last] and nums[mid+1] <= nums[last]:
                    last = mid
                else:
                    first = mid+1
            elif target < nums[mid]:
                if target < nums[first] and nums[first] <= nums[mid]:
                    first = mid+1
                else:
                    last = mid
            elif target == nums[mid]:
                return mid


'''
python good code)
우선 정렬되어 있는지 확인 후 target 조건을 확인(세 수를 한번에 비교)

class Solution:
    # @param {integer[]} numss
    # @param {integer} target
    # @return {integer}
    def search(self, nums, target):
        if not nums:
            return -1

        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) / 2
            if target == nums[mid]:
                return mid

            if nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1
'''

