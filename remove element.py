#Remove Element in Python3

#Approach - 1 :
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums:
            nums.remove(val)
            
            
#Approach - 2 :
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ans = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[ans] = nums[i]
                ans += 1
        return ans
        
 
        
