class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        res = 0
        newlen = len(piles)//3
        piles.sort()
        piles[:] = piles[newlen:]
        print(piles,newlen)
        for i in range(len(piles)):
            if i % 2==0:
                res = res+ piles[i]
        return res