class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        l, r = 0, len(height)-1
        l_max = height[l]
        r_max = height[r]
        while l < r:
            if(l_max < r_max):
                l += 1
                l_max = max(l_max, height[l])
                vol = l_max - height[l]
            else:
                r -= 1
                r_max = max(r_max, height[r])
                vol = r_max - height[r]
                
            if(vol > 0):
                res += vol
        return res