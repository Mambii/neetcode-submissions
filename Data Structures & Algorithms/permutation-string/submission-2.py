class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if(len(s2) < len(s1)):
            return False

        fold1 = [0] * 26
        fold2 = [0] * 26
        

        for i in range(len(s1)):
            fold1[ord(s1[i]) - ord('a')] += 1
            fold2[ord(s2[i]) - ord('a')] += 1
        
        l = 0
        
        for r in range(len(s1), len(s2)):
            if(fold1 == fold2):
                return True
            fold2[ord(s2[r]) - ord('a')] += 1
            fold2[ord(s2[l]) - ord('a')] -= 1
            
            l += 1
        
        if(fold1 == fold2):
            return True
        return False


