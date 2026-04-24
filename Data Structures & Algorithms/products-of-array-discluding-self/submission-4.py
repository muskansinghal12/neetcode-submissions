class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forward = [1]
        backward = [1]
        product = nums[0]
        for i in range(1, len(nums)):
            forward.append(product)
            product = product * nums[i]
        product = nums[len(nums) - 1]
        for i in range(len(nums)-2,-1,-1):
            backward.insert(0,product)
            product = product * nums[i]
        ans = []
        # print(forward)
        # print(backward)
        for i in range(len(nums)):
            ans.append(forward[i]*backward[i])
        return ans
        