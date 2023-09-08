class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        cheapest = 999999
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] < cheapest:
                cheapest = prices[i]
                
            if prices[i] - cheapest > max_profit:
                max_profit = prices[i] - cheapest
            
        return max_profit