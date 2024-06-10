class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        arr = sorted(heights)
        print(arr,heights)
        count = 0
        for i in range(len(arr)):
            if arr[i] != heights[i]:
                count += 1
            
        return count