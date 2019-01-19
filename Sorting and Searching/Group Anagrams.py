#cracking the coding interview 10.2 (p150)
#given an array of strings, group anagrams together
#used sorted() and dictionary

class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        myDict = {}
        
        for i in range(len(strs)):
            word = strs[i]
            word = "".join(sorted(word))
            if word not in myDict:
                myDict[word] = [strs[i]]
            else:
                myDict[word].append(strs[i])
        
        return list(myDict.values())
