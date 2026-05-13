class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        prefix.append(1)
        product = nums[0]
        for i in range(1, len(nums)):
            prefix.append(product)
            product *= nums[i]
        suffix = []
        suffix.append(1)
        product = nums[-1]
        for i in range(len(nums)-2,-1,-1):
            suffix.insert(0,product)
            product *= nums[i]
        ans = []
        for i in range(len(nums)):
            ans.append(prefix[i]*suffix[i])
        return ans

        