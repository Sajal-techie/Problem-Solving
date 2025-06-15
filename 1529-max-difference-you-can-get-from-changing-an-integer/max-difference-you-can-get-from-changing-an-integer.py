class Solution:
    def maxDiff(self, num: int) -> int:
        s = str(num)
        mx = s
        for i in range(len(s)):
            if s[i] != "1" and i == 0:
                mx = s.replace(s[i], "1")
                break
            if s[i] != "0" and s[0] != s[i]:
                mx = s.replace(s[i], "0")
                # if mx[0] == "0":
                #     mx = mx.replace(mx[0], "1", 1)
                break

        mn = s
        print(s)
        for i in range(len(s)):
            if s[i] != "9":
                mn = s.replace(s[i], "9")
                break
        print(mn,mx)
        return int(mn) - int(mx)