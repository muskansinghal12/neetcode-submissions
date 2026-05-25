from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegrees = [0]*numCourses
        graph = [[] for _ in range(numCourses)] 
        for u, v in prerequisites:
            graph[v].append(u)
            indegrees[u] += 1
        ans = []
        q = deque()
        for i in range(numCourses):
            if indegrees[i] == 0:
                ans.append(i)
                q.append(i)
        
        while q:
            course = q.popleft()
            for adj in graph[course]:
                indegrees[adj] -= 1
                if indegrees[adj] == 0:
                    q.append(adj)
                    ans.append(adj)
        
        return ans if len(ans) == numCourses else []
        



        