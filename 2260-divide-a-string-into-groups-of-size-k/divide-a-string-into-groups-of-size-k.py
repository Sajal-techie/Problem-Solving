class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        res = []
        ls = list(s)
        temp = ""
        for i in range(len(ls)):
            if i % k == 0:
                res.append(temp)
                temp = ""
            temp += ls[i]
        res.pop(0)
        print(temp, res)
        while len(temp) < k:
            temp += fill
        print(temp)
        res.append(temp)
        return res