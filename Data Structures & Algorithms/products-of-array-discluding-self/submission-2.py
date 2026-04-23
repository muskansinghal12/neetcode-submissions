class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        start = []
        start.append(nums[0])
        for i in range(1, len(nums)):
            start.append(start[-1]*nums[i])
        last = []
        last.append(nums[-1])
        for i in range(2,len(nums)+1):
            last.insert(0,last[-i+1]*nums[-i])
        print(start)
        print(last)
        ans = []
        ans.append(last[1])
        for i in range(1, len(nums)-1):
            ans.append(start[i-1] * last[i+1])
        ans.append(start[-2])
        return ans   