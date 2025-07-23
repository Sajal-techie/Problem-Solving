class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        res =  0
        ls = list(s)
        print(ls)
        n = len(ls)
        s1 = [ls[0]]
        i = 1
        while i < n:
            curr = ls[i]
            if x >= y:
                if s1 and s1[-1] == 'a' and curr == 'b':
                    s1.pop()
                    res += x
                else:
                    s1.append(curr)
            else:
                if s1 and s1[-1] == 'b' and curr == 'a':
                    s1.pop()
                    res += y
                else:
                    s1.append(curr)
            i += 1
        print('s1', s1)
        if not s1:
            return res
        i = 1
        s2 = [s1[0]]
        while i < len(s1):
            curr = s1[i]
            # print(i, curr, s2, res)
            if x >= y:
                if s2 and s2[-1] == 'b' and curr == 'a':
                    s2.pop()
                    res += y
                else:
                    s2.append(curr)
            else:
                if s2 and s2[-1] == 'a' and curr =='b':
                    s2.pop()
                    res += x
                else:
                    s2.append(curr)
            i += 1
        return res