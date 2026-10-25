class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        maps = {}
        ans = []
        c = 0
        for i, a in enumerate(strs):
            word = "".join(sorted(a))
            if(word in maps):
                ans[maps[word]].append(a)
            else:
                maps[word] = c
                c += 1
                ans.append([a])
        return ans
                