class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}
        length = len(nums)
        for i in range(length):
            if (target-nums[i]) in visited:
                return [visited[target-nums[i]],i]
            visited[nums[i]] = i
        return []

        