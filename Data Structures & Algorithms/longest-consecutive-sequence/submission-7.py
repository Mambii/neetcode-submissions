class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        temp = 1
        if(not nums):
            return 0
        for i in range(1,len(nums)):
            res = max(res,temp)
            if(nums[i] == nums[i-1]):
                continue
            if(nums[i] == nums[i-1] + 1):
                temp += 1
            else:
                
                temp = 1
        res = max(res,temp)
        return res