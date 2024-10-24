# Leetcode 49 (medium) <Group Anagrams> Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# Simple solution: Sort each string and compare if anagram => O(mnlogn) where m is the number of given strings
# Better solution (this code): Use counter array as a key of a dictionary => O(mn*26) where n is the average length of the string and 26 is the maximum length of counter array (alphabets)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myDict = {}

        if len(strs) == 0:
            return []
        elif len(strs) == 1:
            return [strs]

        for str in strs:
            counter = [0] * 26
            for char in str:
                counter[ord(char)-ord("a")] += 1
            counter_key = tuple(counter)
            if counter_key not in myDict:
                myDict[counter_key] = []
            myDict[counter_key].append(str)

        # for anagramGroup in myDict.values():
            # output.append(anagramGroup)
        return list(myDict.values())