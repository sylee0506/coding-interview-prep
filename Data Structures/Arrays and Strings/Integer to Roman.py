#Given an integer, convert it to a roman numeral.
#Input is guaranteed to be within the range from 1 to 3999.

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        str_num = str(num)
        ans = ""
        
        for i in range(-1, -(len(str_num) + 1), -1):
            ans = self.helper(int(str_num[i]), abs(i)) + ans
        
        return ans
    
    def helper(self, n, digit):
        #myDict = {1:"I", 5:"V", 10:"X", 50:"L", 100:"C", 500:"D", 1000:"M"}
        
        if n == 4:
            if digit == 1:
                return ("IV")
            elif digit == 2:
                return ("XL")
            elif digit == 3:
                return ("CD")
        elif n == 9:
            if digit == 1:
                return ("IX")
            elif digit == 2:
                return ("XC")
            elif digit == 3:
                return ("CM")
        else:
            if n < 4:
                ret = ""
                
            if digit == 1:
                if n > 4:
                    ret = "V"
                for i in range(n % 5):
                    ret += "I"
            elif digit == 2:
                if n > 4:
                    ret = "L"
                for i in range(n % 5):
                    ret += "X"
            elif digit == 3:
                if n > 4:
                    ret = "D"
                for i in range(n % 5):
                    ret += "C"
            elif digit == 4:
                for i in range(n // 1):
                    ret += "M"          

            return ret
            '''
            if n < 4 :
                ret = ""
            else:
                ret = myDict[5*(10**(digit-1))]
                
            if digit < 4:
                for i in range(n % 5):
                    ret += myDict[10**(digit-1)]
            elif digit == 4:
                for i in range(n // 1):
                    ret += "M"
            
            return ret
            '''

#more pythonic way) good code!!
'''
class Solution(object):
    def intToRoman(self, num):
        dict = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        result = ""
        for letter, n in zip(dict, nums):
            result += letter * int(num / n)
            num %= n
        return result
'''

#python other code)
#"proper formatting can do the job even better"
'''
M = ["", "M", "MM", "MMM"];
C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"];
X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"];
I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"];
return M[num/1000] + C[(num%1000)/100] + X[(num%100)/10] + I[num%10];
'''
