class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        l = 0
        r = 0
        n = len(nums)
        while r < n-1:
            farthest = 0
            for i in range(l,r+1):
                farthest = max(i+nums[i],farthest)
            l = r+1
            r = farthest
            jumps += 1
        return jumps
        