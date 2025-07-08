class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l = 0
        r = int(sqrt(c))
        if c ==0: return True
        if c ==1: return True
        while l <= r:
            if l * l + r * r == c:
                return True
            elif l * l + r * r > c:
                r = r-1
            else:
                l=l+1
        return False