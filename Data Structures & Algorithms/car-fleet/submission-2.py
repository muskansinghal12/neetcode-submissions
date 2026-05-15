from collections import deque
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # 0 1-  2-  3-  4-  5-  6-  7-  target
        n = len(position)
        times = []
        mapping = []
        stack = []
        for i in range(n):
            mapping.append((position[i],speed[i],(target-position[i])/speed[i]))#p,s,t
        mapping.sort()
        for i in range(n-1,-1,-1):
            p,s,t = mapping[i]
            if stack and stack[-1] >= t:
                continue
            else:
                stack.append(t)
        return len(stack)


        # 0:1, 1:2, 4:4, 7:1
        # 10, 4.5, 3, 3
        # 3 4.5 10 3
        