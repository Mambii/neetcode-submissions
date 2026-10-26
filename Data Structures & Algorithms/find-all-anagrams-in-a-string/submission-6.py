class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        cnt = defaultdict(int)
        scnt = defaultdict(int)
        size = len(p)
        res = []

        if(len(p) > len(s)):
            return res

        for i in range(size):
            cnt[p[i]] += 1
            scnt[s[i]] += 1

        for i in range(len(s) - size + 1):
            if(scnt == cnt):
                res.append(i)

            scnt[s[i]] -= 1
            if(scnt[s[i]] == 0):
                del scnt[s[i]]
                
            if(i + size < len(s)):
                scnt[s[i + size]] += 1
        return res






        return res


