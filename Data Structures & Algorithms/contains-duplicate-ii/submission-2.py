class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        space = {}
        for i, num in enumerate(nums):
            if(num in space and i - space[num] <= k):
                return True
            else:
                space[num] = i
        return False
