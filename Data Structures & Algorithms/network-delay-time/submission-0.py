from collections import deque
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[] for _ in range(n+1)]
        visited = [False]*(n+1)
        for u,v,time in times:
            graph[u].append((v,time))
        
        res = [float('inf')]*(n)
        queue = deque()
        queue.append((k,0))
        res[k-1] = 0
        while queue:
            u, time = queue.popleft()
            for v, t in graph[u]:
                if time+t < res[v-1]:
                    res[v-1] = time+t
                    queue.append((v,time+t))
        ans = -1
        
        for i in range(n):
            if res[i] == float('inf'):
                return -1
            ans = max(ans, res[i])
        return ans


        