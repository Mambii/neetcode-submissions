class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prd = 1
        res = []
        for i in nums:
            prd *= i
        for i in range(len(nums)):
            if(nums[i] != 0):
                res.append(prd//nums[i])
            else:
                placeh = 1
                for k in range(len(nums)):
                    if(k != i):
                        placeh *= nums[k]
                res.append(placeh)
        return res