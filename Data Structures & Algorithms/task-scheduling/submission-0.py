import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq_map = [0]*26
        cycles = 0
        for task in tasks:
            freq_map[ord(task)-ord('A')] += 1
        pq = []
        print(freq_map)
        #max heap
        for task in freq_map:
            if task != 0:
                heapq.heappush(pq, -task)
        print(pq)
        while pq:
            temp = []
            for i in range(0,n+1):
                cycles += 1
                if pq:
                    task = -heapq.heappop(pq)
                    if task-1 != 0:
                        temp.append(-(task-1))
                if not pq and not temp:
                    return cycles
            for t in temp:
                heapq.heappush(pq, t)
            print(pq)
        return cycles
            

        