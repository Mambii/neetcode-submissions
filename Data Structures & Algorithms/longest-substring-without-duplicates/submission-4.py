class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        word = []
        res = 0
        for char in s:
            if(char in word):
                res = max(res,len(word))
                po = word.index(char)
                word = word[po+1:]
            word.append(char)

        res = max(res, len(word))

        return res