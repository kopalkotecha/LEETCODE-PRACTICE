#Can Make Arithmetic Progression from Sequence in Python3

#Approach - 1 : With sorting
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        
        arr.sort()
        diff = arr[1] - arr[0]
        
        for i in range(2,len(arr)):
            if arr[i] - arr[i-1] != diff:
                return False
        
        return True
      
#Approach - 2 : Without Sorting
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        
        length = len(arr)
        min_val = min(arr)
        max_val = max(arr)

        diff = (max_val - min_val) / (length - 1)

        for i in range(length):
            expected = min_val + i * diff
            if expected not in arr:
                return False

        return True
