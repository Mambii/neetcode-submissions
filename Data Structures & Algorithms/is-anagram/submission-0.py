class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars1 = []
        chars2 = []
        for i in s:
            chars1.append(i)
        for i in t:
            chars2.append(i)
        chars1.sort()
        chars2.sort()
        return chars1 == chars2