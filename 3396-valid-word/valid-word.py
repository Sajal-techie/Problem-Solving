class Solution:
    def isValid(self, word: str) -> bool:
        n = len(word)
        bvow = False
        bnvow = False
        bnum = False
        if n < 3:
            return False
        vow = {"a", "e", "i", "o", "u"}
        nvow = {"b", "c", "d","f","g","h", "j", "k","l","m","n","p","q","r","s","t","v","w","x","y","z"}
        num = {"0", "1","2","3","4","5","6","7","8","9"}
        symbol = {'@', '#', '$'}
        for i in symbol:
            if i in word:
                return False
        for i in vow:
            if i in word or i.upper() in word:
                bvow = True
                break
        for i in nvow:
            if i in word or i.upper() in word:
                bnvow = True
                break
        # for i in num:
        #     if i in word:
        #         bnum = True
        #         break
        return all([ bvow, bnvow])
        