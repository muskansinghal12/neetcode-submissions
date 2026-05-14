from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        braces = {')':'(',']':'[','}':'{'}
        stack = deque()
        for bracket in s:
            if bracket in list(braces.values()):
                stack.append(bracket)
            else:
                if stack and stack[-1] == braces[bracket]:
                    stack.pop()
                else:
                    return False
        return True if len(stack) == 0 else False 
        