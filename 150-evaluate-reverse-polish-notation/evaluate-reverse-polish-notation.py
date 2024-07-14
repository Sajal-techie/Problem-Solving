class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+','-','*','/']
        for i in tokens:
            if i in operators:
                stack.append(self.operate(stack.pop(),i,stack.pop()))
            else:
                stack.append(i)
        return int(stack[-1])
            
    def operate(self,num1,operator,num2):
        num1,num2 = int(num1),int(num2)
        if operator == '+':
            return num2 + num1
        elif operator == '-':
            return num2 - num1
        elif operator == '*':
            return num2 * num1
        else:
            return int(num2/num1)