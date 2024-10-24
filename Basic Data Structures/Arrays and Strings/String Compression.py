#cracking the coding interview 1.6 (p91)
#implement a method to perform basic string compression using the counts of repeated characters
#time complexity: O(n) / space complexity: O(1)

class Solution:
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        if len(chars) == 1:
            return len(chars)
        
        temp = chars[0]
        index = 0
        i = 1
        num = 1
        
        while True:
            if i < len(chars) and chars[i] == temp:
                num += 1
            else:
                if num == 1:
                    if i == len(chars):
                        return len(chars)
                    else:
                        temp = chars[i]
                        index = i
                        i += 1
                        continue
                        
                put = i
                for x in str(num):
                    chars.insert(put, x)
                    put += 1
                    
                del chars[index+1:i]
                i = index + len(str(num)) + 1
                
                if i == len(chars):
                    return len(chars)
                else:
                    temp = chars[i]
                    index = i
                    num = 1
                    
            i += 1
