class Solution:
    def helper(self, nums, current_set, ans, used):
        if len(current_set) == len(nums):
            ans.append(current_set[:])
            return
        for i in range(len(nums)):
            if not used[i]:
                used[i] = True
                current_set.append(nums[i])
                self.helper(nums, current_set, ans,used)
                current_set.pop()
                used[i] = False

    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        used = [False]*n
        self.helper(nums, [], ans,used)
        return ans
        