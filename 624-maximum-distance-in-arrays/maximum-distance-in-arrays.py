class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        minVal = arrays[0][0]
        maxVal = arrays[0][-1]
        res = 0
        for i in range(1,len(arrays)):
            start = arrays[i][0]
            end = arrays[i][-1]
            res = max(res, abs(start-maxVal), abs(end-minVal))
            minVal = min(minVal,start)
            maxVal = max(maxVal,end)
        
        return res