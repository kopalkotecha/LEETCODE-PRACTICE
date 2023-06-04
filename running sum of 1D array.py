#Running Sum of 1D Array


#Method - 1
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        ans = [0] * len(nums)    #creating a list with same length as input and initializing all elements to 0 
        ans[0] = nums [0]  #setting first element of output as input
        
        for i in range(1,len(nums)): 
            ans[i] = ans[i-1] + nums[i]   #running sum
        return ans
            
#Method - 2
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]
        return nums
            



      

     
