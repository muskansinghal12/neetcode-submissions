import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = [False]*n
        q = []
        heapq.heappush(q,[0,0])
        cost = 0
        count = 0
        while q and count < n:
            wt, index = heapq.heappop(q)
            if visited[index]:
                continue
            visited[index] = True
            cost += wt
            count = 1
            for i in range(n):
                if index != i:
                    if not visited[i]:
                        heapq.heappush(q,[abs(points[i][0]-points[index][0])+abs(points[i][1]-points[index][1]),i])
        return cost
        