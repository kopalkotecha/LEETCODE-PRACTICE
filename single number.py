#Single Number in Python3

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        uniqueNumber = 0
        
        for i in nums:
            uniqueNumber ^= i;     #using XOR operation
            
        return uniqueNumber
        
'''XOR of zero and some bit returns that bit i.e. x^0 = x...
XOR of two same bits returns 0 i.e. x^x = 0...
And, x^y^x = (x^x)^y = 0^y = y...
XOR all bits together to find the unique number'''
