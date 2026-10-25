class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        low = prices[0]
        high = 0
        for i in range(1,len(prices)):
            if(prices[i] < low):
                low = prices[i]
                high = 0
            high = max(high,prices[i])
            prof = high - low
            if(prof > res):
                res = prof
        return res
            

