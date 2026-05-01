class Solution:
    def combinationSumHelper(self, nums, target, i, current_set, ans):
        if target == 0:
            ans.append(current_set[:])
            return
        if i == len(nums):
            return
        #not take
        self.combinationSumHelper(nums,target,i+1,current_set, ans)
        #take
        if target >= nums[i]:
            current_set.append(nums[i])
            self.combinationSumHelper(nums,target-nums[i],i,current_set, ans)
            current_set.pop()

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        self.combinationSumHelper(nums,target,0,[],ans)
        return ans

        