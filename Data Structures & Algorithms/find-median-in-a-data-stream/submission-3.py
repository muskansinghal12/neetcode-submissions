import heapq
class MedianFinder:

    def __init__(self):
        self.first_half = [] # max_heap
        self.right_half = [] # min_heap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.first_half,-num)
        if self.right_half and -self.first_half[0] > self.right_half[0]:
            heapq.heappush(self.right_half,-heapq.heappop(self.first_half))
        
        if len(self.first_half) > len(self.right_half)+1:
            heapq.heappush(self.right_half,-heapq.heappop(self.first_half))
        elif len(self.right_half) > len(self.first_half):
            heapq.heappush(self.first_half,-heapq.heappop(self.right_half))
        
        

    def findMedian(self) -> float:
        first_length = len(self.first_half)
        right_length = len(self.right_half)
        
        if (first_length + right_length)%2 == 0:
            return (-self.first_half[0] + self.right_half[0])/2
        else:
            return -self.first_half[0]
        
        