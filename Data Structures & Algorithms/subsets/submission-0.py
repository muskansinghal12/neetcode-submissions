class Solution:
    def subsetsHelper(self,nums,i,current_set,ans):
        if i == len(nums):
            new_ans = []
            new_ans.extend(current_set)
            ans.append(new_ans)
            return
            # current_set = []
        current_set.append(nums[i])
        self.subsetsHelper(nums,i+1,current_set,ans)
        current_set.pop()
        self.subsetsHelper(nums,i+1,current_set,ans)
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        current_set = []
        self.subsetsHelper(nums,0,current_set,ans)
        return ans
        