class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ans = set()
        for num in nums:
            ans.add(num)
        return not len(ans) == len(nums)
        