class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        a, b = 'a', 'b'
        if x < y:
            x, y = y, x
            a,b = b, a

        res = c1 = c2 = 0
        for c in s:
            if c == a:
                c1 += 1
            elif c == b:
                if c1:
                    c1 -= 1
                    res += x
                else:
                    c2 += 1
            else:
                res += min(c1, c2) * y
                c1 = c2 = 0
        res += min(c1, c2) * y
        return res