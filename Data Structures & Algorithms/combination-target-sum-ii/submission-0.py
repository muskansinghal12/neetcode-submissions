class Solution:
    def helper(self, nums, start, target, current_set, ans):
        if target == 0:
            ans.append(current_set[:])
            return
        if start == len(nums):
            return
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i-1]:
                continue
            if nums[i] > target:
                break
            current_set.append(nums[i])
            self.helper(nums, i+1, target-nums[i], current_set, ans)
            current_set.pop()
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        self.helper(candidates, 0, target, [], ans)
        return ans
        