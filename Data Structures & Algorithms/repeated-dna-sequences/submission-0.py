class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        test = {}
        res = []
        for i in range(len(s)-9):
            if(s[i:i+10] in test):
                if(test[s[i:i+10]] != 1):
                    res.append(s[i:i+10])
                    test[s[i:i+10]] = 1
            else:
                test[s[i:i+10]] = 0
        return res
            


