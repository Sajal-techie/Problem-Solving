class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = {}
        for i in bills:
            if i == 5:
                change[5] = change.get(5, 0) + 1
            elif i == 10:
                if change.get(5, 0) == 0:
                    return False
                else:
                    change[5] = change.get(5,1) - 1 
                    change[10] = change.get(10,0) + 1
            elif i == 20:
                if change.get(5, 0) == 0 or (change.get(10, 0) == 0 and change.get(5,0) < 3) :
                    return False
                elif change.get(10,0) > 0:
                    change[10] =  change.get(10,1) - 1
                    change[5] = change.get(5,1) - 1
                elif change.get(5,0) >= 3:
                    change[5] = change.get(5,3) - 3
        
        return True
                
