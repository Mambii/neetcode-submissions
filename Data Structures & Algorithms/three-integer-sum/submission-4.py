class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        leng = len(nums)
        res = []
        nums.sort()
        for i in range(len(nums)-2):
            if(i > 0 and nums[i] == nums[i-1]):
                continue
            targ = 0-nums[i]
            l = i+1
            r = leng-1
            while l < r:
                sum = nums[l] + nums[r]
                if(sum< targ):
                    l += 1
                    continue
                elif(sum > targ):
                    r -= 1
                    continue
                else:
                    res.append([nums[i],nums[l],nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l +=1
                    while l < r and nums[r] == nums[r+1]:
                        r-=1
                    
                
        return res


        
        