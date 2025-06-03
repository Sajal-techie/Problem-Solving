class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0 # result 
        l = 0  # left index
        r = len(height) - 1 #right index
        while l < r:  # limiting condition 
            minval = min(height[l],height[r]) # store the minimum value from right and left
            area = (r-l) * minval # find the current area using minvalue and difference of indexes
            res = max(area, res) # find the maximun from current area and previos stored result
            if height[l] <= height[r]: # increase or decresase index based on the condition
                l+=1 
            else:
                r-=1
        return res # res will now have the maximunm area 
        