class Solution:
    def findLucky(self, arr: List[int]) -> int:
        res = []
        tab = {}
        for i in arr:
            if i in tab:
                tab[i] += 1
            else:
                tab[i] = 1
        for k,v in tab.items():
            if k == v:
                res.append(v)
        return max(res) if res else -1