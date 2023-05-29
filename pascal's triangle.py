#Pascal's Triangle in Pyhton3

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]             #result will be 1 for the first row
        
        for i in range(numRows - 1):
            temp = [0] + res[-1] + [0]       #adding 0 on both left and right sides # defining a temporary array to store the values 
            row = []                         
            
            for j in range(len(res[-1]) + 1):     #the length of the next row will be the length of previous row + 1
                row.append(temp[j] + temp[j+1])   # we are just appending the values in the row
            res.append(row)
            
        return res
