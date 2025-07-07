class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = [0] * n 
        right = [0] * n
        curr = 0
        for i in range(n):
            curr = max(curr, height[i])
            left[i] = curr
        print(left,"left")
        curr = 0
        for i in range(n-1, -1, -1):
            curr = max(curr, height[i])
            right[i] = curr
        print(right, "roght")
        res = 0
        for i in range(n):
            curr = min(left[i], right[i]) - height[i]
            if curr > 0:
                res += curr
        return res