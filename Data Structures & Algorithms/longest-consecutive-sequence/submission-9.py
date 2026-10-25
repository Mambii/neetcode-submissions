class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        srs_start =[]
        res = 0
        temp = 1
        uniq = set(nums)
        if(not uniq):
            return 0
        for num in uniq:
            if(num-1) not in uniq:
                srs_start.append(num)
        for i in srs_start:
            h = i
            while h+1 in uniq:
                temp += 1
                h += 1
            res = max(res,temp)
            temp = 1
        return res