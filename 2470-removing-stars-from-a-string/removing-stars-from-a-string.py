class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for ch in s:
            if ch!="*":
                stack.append(ch)
            else:
                if stack:
                    stack.pop()
                else:
                    pass
        ans = ""
        for ch in stack:
            ans+=ch
        return ans
        