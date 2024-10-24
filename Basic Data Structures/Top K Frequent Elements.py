# Leetcode 347 (medium) <Top K Frequent Elements> Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

# Initial solution (this code): dict[num, count] --> sort the dictionay by value => O(n) to make dict + O(nlogn) to sort: O(nlogn) where n is the maximum counter (== the length of input array)
# Better solution: "Bucket sort"; dict[num, count] --> arr[count, [nums]] --> scan the array from tail until reach to k => O(n) to make dict + O(n) to scan: O(n)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return []
        if len(nums) == 1:
            return nums

        myDict = {}
        output = []
        
        for num in nums:
            if num not in myDict:
                myDict[num] = 0
            myDict[num] += 1
        
        # Sort the dictionay by value
        items = sorted(myDict.items(), key = lambda x:x[1], reverse = True)
        
        for item in items:
            output.append(item[0])
            if len(output) == k:
                break

        return output