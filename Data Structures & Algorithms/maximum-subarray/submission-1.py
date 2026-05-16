class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prefix_sum = 0
        ans = -float('inf')
        for num in nums:
            prefix_sum += num
            ans = max(ans, prefix_sum)
            if prefix_sum < 0:
                prefix_sum = 0
        return ans 
        