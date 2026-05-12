import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = []
        #create min heap of distance [distance, [x,y]]
        ans = []
        for x,y in points:
            heapq.heappush(pq, (-(x**2 + y**2),x,y))
            if len(pq) > k:
                heapq.heappop(pq)
        # while pq:
        #     distance, coord = heapq.heappop(pq)
        #     ans.append(coord)
        return [[x,y] for (_,x,y) in pq]


        