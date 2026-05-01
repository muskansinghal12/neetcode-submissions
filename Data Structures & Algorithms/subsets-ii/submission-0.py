class Solution:
    def helper(self, nums, current_set, ans, start):
        # if start == len(nums):
        #     return
        ans.append(current_set[:])
        for i in range(start, len(nums)):
            if i>start and nums[i] == nums[i-1]:
                continue
            current_set.append(nums[i])
            self.helper(nums, current_set, ans, i+1)
            
            current_set.pop()
            
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        self.helper(nums, [], ans, 0)
        return ans

    

        