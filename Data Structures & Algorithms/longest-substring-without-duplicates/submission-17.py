class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 1
        cnt = defaultdict(int)
        look = 0
        if(not s):
            return 0

        l = 0

        for i in range(len(s)):
            if(s[i] not in cnt):
                cnt[s[i]] += 1
            else:
                p = 0
                while p == 0:
                    if(s[l] == s[i]):
                        p = 1
                        l += 1
                    else:
                        del cnt[s[l]]
                        l += 1
                cnt[s[i]] += 1
            res = max(res, i - l + 1)

        



        return res