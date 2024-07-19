class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        ans = []
        for i in range(len(matrix)):
            rowMax = min(matrix[i])
            index = matrix[i].index(rowMax)
            is_lucky = True
            for j in range(len(matrix)):
                if matrix[j][index] > rowMax:
                    is_lucky = False
                    break
            if is_lucky:
                ans.append(rowMax)
        return ans
