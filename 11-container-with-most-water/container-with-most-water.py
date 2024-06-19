class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)-1
        res = 0
        l = 0
        r = n
        while l < r:
            minval = min(height[l],height[r])
            area = (r-l) * minval
            res = max(area, res)
            if height[l] <= height[r]: 
                l+=1 
            else:
                r-=1
        return res