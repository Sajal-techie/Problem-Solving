class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        temp = s1.split() + s2.split()
        res = []
        for i in range(len(temp)):
            val = temp.pop(i)
            if val not in temp:
                res.append(val)
            
            temp.insert(i, val)
        return res