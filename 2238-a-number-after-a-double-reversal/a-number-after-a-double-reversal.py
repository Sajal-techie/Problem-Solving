class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        og = str(num)
        rev = int(og[::-1])
        rev = str(rev)
        dup = rev[::-1]
        dup = int(dup)
        if dup == num :
            return True
        else:
            return False
