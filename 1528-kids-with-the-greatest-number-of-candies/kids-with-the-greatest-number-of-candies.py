class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxs = max(candies)
        return [ x+extraCandies >=maxs for x in candies  ]