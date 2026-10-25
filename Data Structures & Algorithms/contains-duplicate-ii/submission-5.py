class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        space = {}
        for i in range(len(nums)):
            if(nums[i] in space):
                j = space[nums[i]]
                if(abs(i-j) <= k):
                    return True
                space[nums[i]] = i
            else:
                space[nums[i]] = i
        return False
