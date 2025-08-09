class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        while n != 1:
            if n > 1:
                n = n/2
            else:
                return False
        return True