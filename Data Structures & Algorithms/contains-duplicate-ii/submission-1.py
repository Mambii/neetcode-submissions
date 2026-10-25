class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        space = {}
        for i in range(len(nums)):
            j = i + k
            if(nums[i] in nums[i+1:j+1]):
                return True
        return False
