from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #topo sorting
        count = 0
        #1 -> 0
        graph = [[] for _ in range(numCourses)]
        indegrees = [0]*numCourses
        for u, v in prerequisites: #0,1
            graph[v].append(u) #[[0],[]]
            indegrees[u] += 1
        
        q = deque()
        for i in range(numCourses):
            if indegrees[i] == 0:
                count += 1
                q.append(i)
        while q:
            course = q.popleft()
            for adj in graph[course]:
                indegrees[adj] -=1
                if indegrees[adj] == 0:
                    count += 1
                    q.append(adj)
        return count == numCourses
        