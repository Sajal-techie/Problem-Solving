class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n, m = len(s), len(p)
        if m > n: 
            return []
        
        res = []
        p_count = [0] * 26
        s_count = [0] * 26
        
        # helper to map char → index
        def idx(c): 
            return ord(c) - ord('a')
        
        # initialize counts for p and first window
        for i in range(m):
            p_count[idx(p[i])] += 1
            s_count[idx(s[i])] += 1
        
        # compare initial window
        if s_count == p_count:
            res.append(0)
        
        # slide the window
        for i in range(m, n):
            s_count[idx(s[i])] += 1         # add new char
            s_count[idx(s[i - m])] -= 1     # remove old char
            
            if s_count == p_count:          # check only when counts match
                res.append(i - m + 1)
        
        return res