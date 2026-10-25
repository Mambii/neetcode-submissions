class Solution:
    def isPalindrome(self, s: str) -> bool:
            strin = re.sub(r"[^a-zA-Z0-9]", "", s)
            length = len(strin)
            strin = strin.lower()
            if(not strin):
                return True
            return strin == strin[::-1]