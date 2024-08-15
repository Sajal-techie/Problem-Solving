class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives = 0
        tens = 0
        for i in bills:
            if i == 5:
                fives += 1
            elif i == 10:
                if fives <= 0:
                    return False
                else:
                    fives = fives - 1 
                    tens = tens + 1
            elif i == 20:
                if fives <= 0 or (tens <= 0 and fives < 3) :
                    return False
                elif tens > 0:
                    tens =  tens - 1
                    fives = fives - 1
                elif fives >= 3:
                    fives = fives - 3
        
        return True
                
