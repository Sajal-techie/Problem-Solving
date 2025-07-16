class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res, l, lenp, n  = [], 0, len(p), len(s)
        pc = Counter(p)
        print(pc)
        sc = Counter()
        print(sc)
        for i in range(n):
            sc[s[i]] = sc.get(s[i], 0) + 1
            # print(i, sc, s[i], l, res, len(sc)>=lenp, len(sc.values()),len(pc.values()))
            if len(sc) >= lenp:
                if sc == pc:
                    res.append(l)
                sc[s[l]] -= 1
                if sc[s[l]] <= 0:
                    del sc[s[l]]
                l += 1
            elif sum(sc.values()) >= sum(pc.values()):
                if sc == pc:
                    res.append(l)
                sc[s[l]] -= 1
                if sc[s[l]] <= 0:
                    del sc[s[l]]
                l += 1
        return res