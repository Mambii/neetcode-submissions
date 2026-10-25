class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        maps = {}
        fake = {}
        ans=[]
        for i in nums:
            maps[i] = 1 + maps.get(i, 0)
        fake = dict(sorted(maps.items(), key=lambda item: item[1], reverse=True))
        test = list(fake.keys())
        return test[:k]
