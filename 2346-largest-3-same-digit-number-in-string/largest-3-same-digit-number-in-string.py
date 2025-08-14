class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res = -1
        for i in range(1, len(num)-1):
            v1 = num[i]
            v2 = num[i-1]
            v3 = num[i+1]
            if v1 == v2 == v3:
                res = max(res, int(v1*3))
                if res == 999:
                    break
        if res == 0:
            return "000"
        if res < 0:
            return ""
        return str(res)