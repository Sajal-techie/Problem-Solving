class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        map = {"a": -1, "b": -1, "c": -1}
        res = 0
        for i in range(len(s)):
            if i > map.get(s[i]):
                map[s[i]] = i
            if map.get("a") != -1 and map.get("b") != -1 and map.get("c") != -1:
                temp = min(map.get("a"), map.get("b"), map.get("c"))  + 1
                res += temp
        return res