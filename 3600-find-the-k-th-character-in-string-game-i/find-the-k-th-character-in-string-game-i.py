class Solution:
    def kthCharacter(self, k: int) -> str:
        s = "a"
        while len(s) < k:
            temp = [chr(ord(x)+1) for x in s]
            temp = "".join(temp)
            s += temp
        return s[k-1]
