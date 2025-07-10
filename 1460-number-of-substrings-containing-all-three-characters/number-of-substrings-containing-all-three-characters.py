class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        map = {"a": -1, "b": -1, "c": -1}
        res = 0
        for i in range(len(s)):
            map[s[i]] = i
            temp = min(map.values())  + 1
            res += temp
        return res