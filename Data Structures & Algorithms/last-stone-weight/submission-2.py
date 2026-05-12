import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pq = [-x for x in stones]
        heapq.heapify(pq)
        while len(pq) > 1:
            y = -heapq.heappop(pq)
            x = -heapq.heappop(pq)
            if x != y:
                heapq.heappush(pq, -(y-x))
        if len(pq) == 0:
            return 0
        return -pq[0]

        