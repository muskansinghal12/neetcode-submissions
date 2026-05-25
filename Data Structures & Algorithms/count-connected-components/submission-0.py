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
                self.dfs(i,visited, graph)
        return count



        