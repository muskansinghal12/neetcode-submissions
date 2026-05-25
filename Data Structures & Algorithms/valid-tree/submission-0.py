from collections import deque
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #atleast it should have n-1 edges
        #it should be connected
        #there should be no cycles
        if len(edges) < n-1: #atleast it should have n-1 edges
            return False
        
        graph = [[] for _ in range(n)]
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited = [False]*n

        queue = deque() #(vertex, parent)
        queue.append((0,-1))
        visited[0] = True
        n -= 1 # to check all the nodes are visited or not
        while queue:
            v, parent = queue.popleft()
            for adj in graph[v]:
                if visited[adj] and adj != parent:
                    return False
                elif not visited[adj]:
                    queue.append((adj,v))
                    visited[adj] = True
                    n -= 1
        
        return True if n == 0 else False


        