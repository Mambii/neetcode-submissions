class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        res = []
        for i in range(len(code)):
            ans = 0
            if(k>0):
                for j in range(i+1, i+k+1):
                    ans += code[j%len(code)]
                res.append(ans)
            elif(k<0):
                for j in range(i+k, i):
                    ans += code[j%len(code)]
                res.append(ans)
            else:
                res.append(0)
        return res