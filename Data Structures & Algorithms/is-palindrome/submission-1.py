class Solution:
    def isPalindrome(self, s: str) -> bool:
            strin = re.sub(r"[^a-zA-Z0-9]", "", s)
            length = len(strin)
            strin = strin.lower()
            if(not strin):
                return True
            for i in range(length//2+1):
                let1 = strin[i]
                let2 = strin[-1-i]
                #print(let1,let2)
                if(let1 != let2):
                    return False
            return True