class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        res = 0
        first = points.pop(0)
        for i in points:
            temp = max(abs(i[0]-first[0]), abs(i[1]-first[1]))
            first = i
            res += temp
        return res