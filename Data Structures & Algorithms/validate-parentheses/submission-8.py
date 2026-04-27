from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        for ch in s:
            if ch in ('(','{','['):
                stack.append(ch)
            else:
                if stack:
                    bracket = stack.pop()
                    if ch is ')' and bracket is not '(':
                        return False
                    if ch is ']' and bracket is not '[':
                        return False
                    if ch is '}' and bracket is not '{':
                        return False
                else:
                    return False
        if len(stack) == 0:
            return True
        return False
                

                    

        