class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = [0]
        for i in range(1, n):
            while len(stack)>0 and temperatures[stack[-1]] < temperatures[i]:
                curent = stack.pop()
                res[curent] = i-curent
            stack.append(i)
        return res

