class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        i = 1
        direction = 'forward'
        while time > 0:
            print(time,i,direction)
            if i <= n and i >=1 :
                if direction == 'forward':
                    i += 1
                    time -= 1
                else:
                    i -= 1
                    time -= 1
            if i == n:
                direction = 'backward'
            if i == 1:
                direction = 'forward'
            
        return i