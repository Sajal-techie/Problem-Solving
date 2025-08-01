class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]*x for x in range(1, numRows + 1)]
        print(res)
        if numRows < 2:
            return res
        prev = res[1]
        print(prev)
        for i in range(2, numRows):
            for j in range(1,len(res[i])-1):
                # print(i,j, res[i-1][j] + res[i-1][j-1])
                res[i][j] = res[i-1][j] + res[i-1][j-1]
        return res