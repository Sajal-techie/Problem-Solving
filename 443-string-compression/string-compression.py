class Solution:
    def compress(self, chars: List[str]) -> int:
        count = 1
        res = []
        for i in range(len(chars)):
            if i + 1 < len(chars) and chars[i] == chars[i+1]:
                    count = count+1
                    chars[i]
                # else:
                #     res.append(chars[i])
                #     if count != 1:
                #         val = str(count)
                #         for j in val:
                #             res.append(str(j))
                #     count = 1
            else:
                res.append(chars[i])
                if count != 1:
                    val = str(count)
                    for j in val:
                        res.append(str(j))
                count = 1
        chars[:] = res
        return len(res)
                        