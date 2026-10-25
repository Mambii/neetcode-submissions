class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapy={}
        
        for i in range(len(nums)):
            mapy[nums[i]] = i
            
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in mapy and i != mapy[diff]:
                ans =[i, mapy[diff]]
                return ans