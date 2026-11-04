class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        res = 0
        
        if(len(s2) < len(s1)):
            return False

        fold1 = defaultdict(int)
        fold2 = defaultdict(int)
        

        for i in range(len(s1)):
            fold1[s1[i]] += 1
            fold2[s2[i]] += 1
        
        l = 0
        
        for r in range(len(s1), len(s2)):
            if(fold1 == fold2):
                return True
                break
            fold2[s2[r]] += 1
            fold2[s2[l]] -= 1
            if fold2[s2[l]] == 0:
                del fold2[s2[l]]
            l += 1
        
        if(fold1 == fold2):
            return True
        print(fold1,fold2)
        return False


