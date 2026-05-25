from collections import deque
class Solution:
    def dfs(self, i, visited, graph):
        visited[i] = True
        for adj in graph[i]:
            if not visited[adj]:
                self.dfs(adj, visited, graph)
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = [False]*n
        graph = [[] for _ in range(n)]
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        count = 0
        for i in range(n):
            if not visited[i]:
                count += 1
                stack = deque()
                # stack = [i]
                stack.append(i)
                while stack:
                    u = stack.pop()
                    if visited[u]:
                        continue
                    visited[u] = True
                    for adj in graph[u]:
                        if not visited[adj]:
                            stack.append(adj)
        return count



        