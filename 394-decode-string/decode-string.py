class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in s:
            if i.isdigit():
                if stack and type(stack[-1]) == int:
                    stack.append(int(str(stack.pop()) + i))
                else:
                    stack.append(int(i))
            elif i != ']':
                stack.append(i)
            else:
                temp = ''
                while stack:
                    if stack[-1] != '[':
                        temp  = stack.pop() + temp
                    else:
                        break
                stack.pop()
                stack.append(stack.pop() * temp)
        return "".join(stack)            
            
                
            