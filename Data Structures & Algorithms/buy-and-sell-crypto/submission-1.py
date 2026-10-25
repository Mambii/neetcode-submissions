class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        low = prices[0]
        high = 0
        for i in range(1,len(prices)):
            if(prices[i] < low):
                low = prices[i]
            else:
                prof = prices[i] - low
                res = max(res, prof)
            
        return res
            

