class Solution:
    def kMirror(self, k: int, n: int) -> int:
        left, total = 1, 0
    
        while n > 0:
            for i in range(left, left * 10):
                if n<=0:
                    break
                val = self.create_pallindrome(i, True)
                if self.is_pallindrome(val, k):
                    total += val
                    n -= 1
            for i in range(left, left*10):
                if n<= 0:
                    break
                val = self.create_pallindrome(i, False)
                if self.is_pallindrome(val, k):
                    total += val
                    n-=1
            left *= 10
        return total

    
    def create_pallindrome(self, num, odd):
        x = num
        if odd:
            x = x // 10
        while x > 0:
            num = num * 10 + x % 10
            x //= 10
        return num
    def is_pallindrome(self, n, base):
        if n == 0:
            return 0
        digits = []
        while n > 0:
            digits.append(n % base)
            n //= base
        return digits == digits[::-1]
