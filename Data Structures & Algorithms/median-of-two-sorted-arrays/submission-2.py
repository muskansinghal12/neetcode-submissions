class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        low = 0
        high = len(nums1)
        total_length = len(nums1) + len(nums2)
        while low <= high:
            mid = (low+high) // 2
            px = mid
            py = ((total_length+1) // 2) - mid
            x1 = -float('inf')
            x2 = -float('inf')
            x3 = float('inf')
            x4 = float('inf')
            if px > 0:
                x1 = nums1[px-1]
            if py > 0:
                x2 = nums2[py-1]
            if px < len(nums1):
                x3 = nums1[px]
            if py < len(nums2):
                x4 = nums2[py]
            if x1 <= x4 and x2 <= x3:
                if total_length%2 == 0:
                    return (max(x1,x2) + min(x3,x4))/2
                else:
                    return max(x1,x2)
            elif x1 > x4:
                high = mid - 1
            else:
                low = mid + 1
        return -1
                


        