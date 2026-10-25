class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        c = 0
        for a in strs:
            count = [0] *26
            for c in a:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(a)
        return list(ans.values())
                