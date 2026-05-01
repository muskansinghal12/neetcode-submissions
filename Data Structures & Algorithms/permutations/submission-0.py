class Solution:
    def helper(self, nums, current_set, ans):
        if len(current_set) == len(nums):
            ans.append(current_set[:])
            return
        for i in nums:
            if i not in current_set:
                current_set.append(i)
                self.helper(nums, current_set, ans)
                current_set.pop()

    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.helper(nums, [], ans)
        return ans
        