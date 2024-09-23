class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        table = {} 
        res = 0
        for row in grid:
            rowtuple = tuple(row)
            table[rowtuple] = table.get(rowtuple, 0) + 1
        
        for col in zip(*grid):
            coltuple = tuple(col)
            if coltuple in table:
                res += table.get(coltuple)
        return res
        