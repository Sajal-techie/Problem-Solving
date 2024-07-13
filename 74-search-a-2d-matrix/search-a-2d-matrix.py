class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix)-1
        while l <= r:
            mid = (l+r)//2
            if matrix[mid][0] <= target and matrix[mid][len(matrix[mid])-1] >= target:
                print('hai')
                break
            elif matrix[mid][0] > target:
                r = mid- 1 
            else:
                l = mid + 1
            
        row = (l+r)//2
        l = 0
        r = len(matrix[row])-1
        while l <= r:
            mid = (l+r)//2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                r = mid - 1
            else:
                l = mid + 1