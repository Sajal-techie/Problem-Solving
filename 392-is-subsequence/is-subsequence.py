class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i,j = 0,0
        if s==t: return True
        if not t: return False
        if not s: return True
        while i < len(t) and j < len(s):
            if t[i] == s[j]:
                j+=1
            i+=1
        return j == len(s)
