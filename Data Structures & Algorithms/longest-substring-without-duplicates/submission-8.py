class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        res = 0
        seen = set()
        left = 0
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[left])
                left += 1
            res = max(r-left+1, res)
            seen.add(s[r])
        


        return res