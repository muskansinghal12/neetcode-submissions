
from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        open_brackets = ['(','{','[']
        open_close_map = {}
        open_close_map[')'] = '('
        open_close_map['}'] = '{'
        open_close_map[']'] = '['
        stack = deque()
        for bracket in s:
            if bracket in open_brackets:
                stack.append(bracket)
            else:
                if len(stack) > 0 and stack[-1] == open_close_map[bracket]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
            


        