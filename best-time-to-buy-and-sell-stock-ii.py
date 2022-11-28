class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if not prices or len(prices) >= 30000:
            return 0
        
        result = 0
        for i in range(0, len(prices)-1):
            if prices[i+1] > prices[i]:
                result += prices[i+1] - prices[i]
            

        return result
