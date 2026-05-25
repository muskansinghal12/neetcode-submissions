import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[] for _ in range(n+1)]
        visited = [False]*(n+1)
        for u,v,time in times:
            graph[u].append((v,time))
        
        dist = [float('inf')]*(n+1)
        queue = []
        heapq.heappush(queue,(0,k))
        dist[k] = 0
        while queue:
            time, u= heapq.heappop(queue)
            if time > dist[u]:
                continue
            for v, t in graph[u]:
                if t+dist[u] < dist[v]:
                    dist[v] = t+dist[u]
                    heapq.heappush(queue,(dist[v],v))
        ans = max(dist[1:])
        
        
        return ans if ans < float('inf') else -1


        