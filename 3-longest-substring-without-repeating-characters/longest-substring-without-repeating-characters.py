class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n < 2:
            return n
        temp = s[0]
        ans = 1
        for i in range(1, len(s)):
            while s[i] in temp:
                temp = temp[1:i]
            temp += s[i]
            ans = max(len(temp), ans)
        return ans