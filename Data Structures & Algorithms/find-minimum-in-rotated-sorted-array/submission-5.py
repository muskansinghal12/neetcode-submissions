class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums)-1
        ans = float('inf')
        while low <= high:
            mid = int((low+high)/2)
            if nums[low] <= nums[mid]:
                #sorted part
                ans = min(ans, nums[low])
                #search in other unsorted part
                low = mid+1
            else:
                ans = min(ans, nums[mid])
                high = mid-1
        return ans

        