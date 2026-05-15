from collections import deque
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = ["+",'-','*','/']
        stack = []
        for ch in tokens:
            if ch in operands:
                op1 = stack.pop()
                op2 = stack.pop()
                res = 0
                if ch == '+':
                    res = op1+op2
                elif ch == '-':
                    res = op2-op1
                elif ch == '*':
                    res = op1*op2
                else:
                    res = int(op2/op1)
                stack.append(res)
            else:
                stack.append(int(ch))
        return stack[-1]

        