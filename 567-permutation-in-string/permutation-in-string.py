class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s2c = [0] * 26
        s1c = [0] * 26
        n,m = len(s2), len(s1)
        if n < m:
            return False
        def idx(c):
            return ord(c) - ord('a')
        for i in range(len(s1)):
            s1c[idx(s1[i])] += 1 
            s2c[idx(s2[i])] += 1
        print(s1c, s2c)
        if s1c == s2c:
            return True
        for i in range(n-m):
            s2c[idx(s2[i+m])] += 1
            s2c[idx(s2[i])] -= 1
            if s1c == s2c:
                return True
        return False