class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        ls = list(s)
        res = []
        temp = ""
        for i in range(len(ls)):
            if temp and i % k == 0:
                res.append(temp)
                temp = ""
            temp += ls[i]
        print(temp, res)
        while len(temp) < k:
            temp += fill
        print(temp)
        res.append(temp)
        return res