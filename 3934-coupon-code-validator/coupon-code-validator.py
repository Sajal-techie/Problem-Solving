class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        resmap = {
            "electronics": [],
            "grocery": [],
            "pharmacy": [], 
            "restaurant": []
        }
        res = []
        def is_validcode(s):
            return all(c.isalnum() or c == '_' for c in s)
        for i in range(len(code)):
            # print(is_validcode(code[i]), isActive[i], code[i])
            if isActive[i] and code[i] and businessLine[i] in ["electronics", "grocery", "pharmacy", "restaurant"] and is_validcode(code[i]):
                resmap[businessLine[i]].append(code[i])
        print(resmap)
        for j in resmap.values():
            j.sort()
            res.extend(j)
        return res