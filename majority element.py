#Majority Element in Python3

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        ans = len(nums) // 2
        temp = set(nums)
        
        for i in temp:
            if nums.count(i) > ans:
                return i
         
