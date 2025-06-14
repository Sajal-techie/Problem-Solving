class Solution:
    def minMaxDifference(self, num: int) -> int:
        s = str(num)
        mn = 0
        mx = 0
        for i in range(len(s)):
            if mn and mx:
                break
            if s[i] != "9":
                if not mx:
                    mx = s.replace(s[i], "9")
            if s[i] != 0:
                if not mn:
                    mn = s.replace(s[i], "0")
        print(mx, mn)
        if mx == 0:
            mx = num
        return int(mx) - int(mn)