class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = {} #num : index
        for i, num in enumerate(nums):
            if (target - num) in mapping:
                return [mapping[target-num],i]
            mapping[num] = i
        return -1

