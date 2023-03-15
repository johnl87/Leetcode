# lc 121
class Solution:
    def maxProfit(prices: list[int]) -> int:
        left, right = 0, 1 #day 0 and day 1
        maxProfit = 0
        
        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                maxProfit = max(maxProfit,profit)
            else:
                left = right
            right+=1 #advancing the right ptr
        return maxProfit
            
    
    
    prices = [7,1,5,3,6,4]
    print(maxProfit(prices))