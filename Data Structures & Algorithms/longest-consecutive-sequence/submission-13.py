class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        srs_start =[]
        res = 0
        temp = 1
        uniq = set(nums)
        if(not uniq):
            return 0
        streak = 1
        curr = 0
        for num in uniq:
            if(num-1 not in uniq):
                curr = num
                streak = 1

            while curr+1 in uniq:
                streak += 1
                curr += 1
            res = max(res,streak)
        return res