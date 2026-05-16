from collections import deque
class Solution:
    def checkValidString(self, s: str) -> bool:
        stack_left = deque()
        stack_star = deque()
        for i, ch in enumerate(s):
            if ch == '(':
                stack_left.append(i)
            elif ch == '*':
                stack_star.append(i)
            else:
                if not stack_left and not stack_star:
                    return False
                elif stack_left:
                    stack_left.pop()
                elif stack_star:
                    stack_star.pop()
        while stack_left:
            if not stack_star or stack_star[-1] < stack_left[-1]:
                return False
            stack_star.pop()
            stack_left.pop()
        return True if not stack_left else False
        