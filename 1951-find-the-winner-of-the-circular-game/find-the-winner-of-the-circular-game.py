class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        frnd = [x for x in range(n)]
        temp = k
        i=0
        while len(frnd) > 1:
            if temp == 0:
                temp = k
            temp -= 1
            if temp == 0:
                frnd.pop(i)
            else:
                i+=1
            if i >= len(frnd):
                i = 0
        
        return frnd.pop() + 1

