# from collections import deque
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # 0 1-  2-  3-  4-  5-  6-  7-  target
        n = len(position)
        times = []
        mapping = []
        # stack = []
        for i in range(n):
            mapping.append((position[i],speed[i],(target-position[i])/speed[i]))#p,s,t
        mapping.sort()
        fleets = 0
        prev_time = 0
        for i in range(n-1,-1,-1):
            p,s,t = mapping[i]
            if t > prev_time:
                fleets += 1
                prev_time = t
        return fleets

        