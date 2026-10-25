class Solution:

    def encode(self, strs: List[str]) -> str:
        if(strs == [""]):
            return '-'
        if(not strs):
            return ''
        en_s = "♥".join(strs)
        return en_s

    def decode(self, s: str) -> List[str]:
        if(s == '-'):
            return [""]
        if(not s):
            return []
        de_s = s.split("♥")
        return de_s