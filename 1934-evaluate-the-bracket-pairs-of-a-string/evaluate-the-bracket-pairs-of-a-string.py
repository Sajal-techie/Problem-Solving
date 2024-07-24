class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        temp = dict((itm[0] , itm[1]) for itm in knowledge )
        stack = ''
        res = ''
        i = 0
        while i < len(s):
            if s[i] == '(':
                i+=1
                while s[i] != ')':
                    stack += s[i]
                    i+=1
                if stack in temp:
                    res +=temp[stack]
                else:
                    res += '?'
                stack = ''
            elif s[i]==')':
                i+=1
            else:
                res += s[i]
                i+=1
            
        return res
