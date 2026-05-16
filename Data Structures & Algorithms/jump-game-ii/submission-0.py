class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        ans = [float('inf')]*n
        ans[0] = 0
        for i in range(n):
            for j in range(1,nums[i]+1):
                if i+j < n:
                    ans[i+j] = min(ans[i+j],ans[i]+1)
        # print(ans)
        return int(ans[-1])

        