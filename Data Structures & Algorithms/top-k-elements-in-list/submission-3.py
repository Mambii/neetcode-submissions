class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        maps = {}
        long = len(nums)
        ans=[[] for i in range(len(nums)+1)]
        rans = []
        for i in nums:
            maps[i] = 1 + maps.get(i, 0)
        for n, c in maps.items():
            ans[c].append(n)
        for i in range(len(ans)-1, 0, -1):
            for n in ans[i]:
                rans.append(n)
                if(len(rans) == k):
                    return rans


