from collections import deque
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #atleast it should have n-1 edges
        #it should be connected
        #there should be no cycles
        if len(edges) != n-1: #atleast it should have n-1 edges
            return False
        
        graph = [[] for _ in range(n)]
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited = [False]*n

        queue = deque() #(vertex, parent)
        queue.append(0)
        visited = set()
        visited.add(0)
        
        while queue:
            v = queue.popleft()
            for adj in graph[v]:
                if adj not in visited:
                    queue.append(adj)
                    visited.add(adj)
        
        return len(visited) == n


        