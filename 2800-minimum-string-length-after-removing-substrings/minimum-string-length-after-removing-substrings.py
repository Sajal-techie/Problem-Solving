class Solution:
    def minLength(self, s: str) -> int:
        while True:
            if 'AB' in s:
                s = s.replace('AB','')
            elif 'CD' in s:
                s = s.replace('CD','')
            else:
                return len(s)