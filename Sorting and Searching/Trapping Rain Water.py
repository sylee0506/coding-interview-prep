#Google former coding interview question
#Find the volume of each lake created by rainwater
#Leetcode #42.Trapping Rain Water
#Time complexity: O(n)
#Space complexity: O(1)

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        left = 0
        right = len(height)-1
        left_w = right_w = water = 0
        
        while left < right:
            if height[left] <= height[right]:
                left_w = max(left_w, height[left])
                water += (left_w - height[left])
                left += 1
            else:
                right_w = max(right_w, height[right])
                water += (right_w - height[right])
                right -= 1
        
        return water
