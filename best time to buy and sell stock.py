#Best Time to Buy and Sell Stock in Python3

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        min_price = prices[0]
        max_profit = 0
        temp = 0
        
        for i in range(1,len(prices)):
            min_price = min(min_price,prices[i])
            
            if prices[i] < prices[i-1]:
                temp += 1
            else:
                diff = prices[i] - min_price
                max_profit = max(max_profit,diff)
                
        if temp == len(prices):
            return 0
        else:
            return max_profit
      
