class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        min_n = 9999999999
        profit = 0
        for num in prices:
            if num < min_n:
                min_n = num
            if num - min_n > profit:
                profit = num - min_n
            
        return profit
            
        