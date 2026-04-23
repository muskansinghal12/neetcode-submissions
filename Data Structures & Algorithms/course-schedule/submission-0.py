from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        indegrees = [0]*numCourses
        for u, v in prerequisites:
            graph[v].append(u)
            indegrees[u] += 1
        
        q = deque()
        count = 0
        for i in range(numCourses):
            if indegrees[i] == 0:
                count += 1
                q.append(i)
        while q:
            node = q.popleft()
            for adj in graph[node]:
                indegrees[adj] -= 1
                if indegrees[adj] == 0:
                    count += 1
                    q.append(adj)
        return count == numCourses



        