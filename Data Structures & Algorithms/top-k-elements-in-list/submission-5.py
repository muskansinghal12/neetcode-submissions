import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if num not in freq:
                freq[num] = 0
            freq[num] += 1
        pq = []
        for key, val in freq.items():
            heapq.heappush(pq,[val,key])
            if len(pq) > k:
                heapq.heappop(pq)
        ans = []
        while pq:
            ans.append(heapq.heappop(pq)[1])
        return ans

        

            
        