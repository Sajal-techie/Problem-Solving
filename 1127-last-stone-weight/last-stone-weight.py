class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pr = []
        other = []
        stones.sort(reverse=True)
        if len(stones) <= 1:
            return stones[0]
        pr = stones[0:2]
        stones = stones[2:] if len(stones) > 2 else []
        print(pr, stones)
        while pr:
            # print(pr, stones)
            v1, v2 = pr
            if v1 == v2:
                pr = stones[:2] if len(stones) > 1 else []
                if pr:
                    stones = stones[2:]
            else:
                v3 = v1 - v2
                stones.append(v3)
                stones.sort(reverse=True)
                pr = stones[:2] if len(stones) > 1 else []
                if pr:
                    stones = stones[2:]
        return stones[0] if stones else 0
