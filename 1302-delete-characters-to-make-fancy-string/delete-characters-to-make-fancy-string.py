class Solution:
    def makeFancyString(self, s: str) -> str:
        res = s[0]
        c = 1
        for i in range(1, len(s)):
            if s[i] == res[-1]:
                c += 1
                if c < 3:
                    res += s[i]
            else:
                c = 1
                res += s[i]
        return res