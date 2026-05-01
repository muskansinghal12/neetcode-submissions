class Solution:
    def subsetXORSumHelper(self, nums, i, xor):
        if i==len(nums):
            return xor
        take = self.subsetXORSumHelper(nums,i+1,xor^nums[i])
        not_take = self.subsetXORSumHelper(nums,i+1,xor)
        return take+not_take
    def subsetXORSum(self, nums: List[int]) -> int:
        return self.subsetXORSumHelper(nums,0,0)
    

        