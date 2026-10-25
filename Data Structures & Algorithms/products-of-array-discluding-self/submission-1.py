class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        suf = [0] * len(nums)
        pref = [0] * len(nums)
        res = []
        suf[-1] = 1
        pref[0] = 1
        for i in range(1,len(nums)):
            pref[i] = pref[i-1] * nums[i-1]
            suf[-1-i] = suf[-i] * nums[-i]
        for i in range(len(nums)):
            res.append(pref[i]*suf[i])

    
        return res