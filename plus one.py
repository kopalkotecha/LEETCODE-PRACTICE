#Plus one in Python3

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        temp = ""          #empty string
        
        for i in range(len(digits)):
            temp += str(digits[i])     #add values into the string
            
        num = int(temp)   #converting string into integer
        ans = num + 1     #adding 1 to the number
        ans = str(ans)    #converting back to string
        
        return [int(i) for i in ans]  #returning array by converting into integer
        
    
