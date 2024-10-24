# Leetcode 238 (medium) <Product of Array Except Self> Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i]. The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# Requirement: You must write an algorithm that runs in O(n) time and without using the division operation.
# Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)

# Clever solution: "Prefix-Postfix" => O(n) to create prefix + O(n) to create postfix: O(n)
# Optimize space (this code): Don't create prefix and postfix array; just do it directly on the output!

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)

        # Pass 1: Prefix
        prefix = 1
        for i in range(len(nums)):
            if i == 0:
                continue
            else:
                output[i] = prefix * nums[i-1]
                prefix = output[i]
        
        # Pass 2: Postfix
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                continue
            else:
                postfix *= nums[i+1]
                output[i] *= postfix
    
        return output