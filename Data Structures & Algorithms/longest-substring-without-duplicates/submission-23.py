class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 1
        cnt = {}
        look = 0
        if(not s):
            return 0

        l = 0

        for i, char in enumerate(s):
            if(char in cnt and cnt[char] >= l):
                l = cnt[char] + 1
            
            cnt[char] = i
            res = max(res, i - l + 1)

        return res