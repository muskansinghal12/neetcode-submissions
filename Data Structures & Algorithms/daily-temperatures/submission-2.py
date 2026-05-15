from collections import deque
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = []
        for i in range(len(temperatures)-1,-1,-1):
            while stack and stack[-1][1] <= temperatures[i]:
                stack.pop()
            if len(stack) == 0:
                ans.insert(0,0)
            else:
                ans.insert(0,stack[-1][0]-i)
            stack.append((i, temperatures[i]))
        return ans



        