import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if num not in freq:
                freq[num] = 0
            freq[num] += 1
        # print(freq)
        pq = []
        for num, fre in freq.items():
            heapq.heappush(pq,[fre,num])
            if len(pq) > k:
                heapq.heappop(pq)
            
        ans = []
        # print(freq)
        while pq:
            fre, num = heapq.heappop(pq)
            ans.append(num)
        return ans


        