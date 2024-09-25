class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack, n = [], len(asteroids) 
        stack.append(asteroids[0])
        for i in range(1,n):
            while stack and asteroids[i] < 0 and stack[-1] > 0:
                if abs(stack[-1]) < abs(asteroids[i]):
                    stack.pop()
                elif abs(stack[-1]) > abs(asteroids[i]):
                    break
                else:
                    stack.pop()
                    break
            else:
                stack.append(asteroids[i])
        return stack
                