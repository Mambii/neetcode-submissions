class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        cnt = defaultdict(int)
        size = len(p)
        res = []

        if(len(p) > len(s)):
            return res

        for i in p:
            cnt[i] += 1

        l, r = 0, size
        scnt = defaultdict(int)

        for i in range(r):
            scnt[s[i]] += 1

        for i in range(len(s)-r+1):
            if(scnt == cnt):
                res.append(i)

            scnt[s[i]] -= 1
            if(scnt[s[i]] == 0):
                del scnt[s[i]]
                
            if(i+r < len(s)):
                scnt[s[i+r]] += 1
        return res






        return res


