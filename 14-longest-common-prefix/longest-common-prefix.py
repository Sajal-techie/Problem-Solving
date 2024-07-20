class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = []
        if len(strs) == 1:
            return strs[0]
        word = strs.pop()
        for i in range(len(strs)):
            temp = ''
            for j in range(len(strs[i])):
                if j < len(word) and strs[i][j] == word[j]:
                    temp += word[j]
                else:
                    res.append(temp)
                    break
            else:
                res.append(temp)
        return min(res) if res else ""
