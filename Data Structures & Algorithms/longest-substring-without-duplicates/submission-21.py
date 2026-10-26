class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 1
        cnt = {}
        look = 0
        if(not s):
            return 0

        l = 0

        for i in range(len(s)):
            if(s[i] in cnt and cnt[s[i]] >= l):
                l = cnt[s[i]] + 1
            
            cnt[s[i]] = i
            res = max(res, i - l + 1)

        return res