import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #range of k -> 1 to max in the pile
        ans = float('inf')
        low = 1
        high = max(piles)
        while low <= high:
            mid = int((low+high)/2)
            hours = self.calculate_hours(piles, mid)
            print(mid)
            if hours <= h:
                ans = min(ans, mid)
                high = mid-1
            else:
                low = mid + 1
        
        return ans

        
    def calculate_hours(self, piles, k):
        hours = 0
        for banana in piles:
            hours += math.ceil(banana/k)
        # print(hours)
        return hours
        