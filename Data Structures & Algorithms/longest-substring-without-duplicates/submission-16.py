class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 1
        cnt = defaultdict(int)
        look = 0
        if(not s):
            return 0

        l, r = 0, 0

        for i in range(len(s)):
            if(s[i] not in cnt):
                cnt[s[i]] += 1
                look += 1
            else:
                res = max(res, look)
                p = 0
                while p == 0:
                    if(s[l] == s[i]):
                        p = 1
                        l += 1
                    else:
                        del cnt[s[l]]
                        l += 1
                        look -= 1

                cnt[s[i]] += 1
        res = max(res, look)
        



        return res