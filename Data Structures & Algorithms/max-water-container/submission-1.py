class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        i = 0
        j = len(heights) - 1
        while i < j:
            less = min(heights[j], heights[i])
            vol = (j-i) * less
            res = max(res,vol)
            if(less == heights[i]):
                i += 1
            elif(less == heights[j]):
                j -= 1
        return res