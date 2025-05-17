class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])
        res = []
        visited = set()
        i, j = 0, 0 
        dr = "R"
        print(matrix, n, m)
        while len(res) < n * m:
            if (i,j) not in visited:
                visited.add((i, j))
                res.append(matrix[i][j])
            if dr == "R":
                if j+1 < m and (i, j+1) not in visited:
                    j += 1
                else:
                    dr = "D"
            if dr == "D":
                if i+1 < n and (i+1, j) not in visited:
                    i += 1
                else:
                    dr = "L"
            if dr == "L":
                if j > 0 and (i, j-1) not in visited:
                    j -= 1
                else:
                    dr = "U"
            if dr == "U":
                if i > 0 and (i-1, j) not in visited:
                    i -= 1
                else:
                    dr = "R"

        return res