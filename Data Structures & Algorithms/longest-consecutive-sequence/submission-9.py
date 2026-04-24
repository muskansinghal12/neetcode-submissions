class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hs = set(nums)
        ans = 0
        for num in nums:
            if num-1 not in hs:
                count = 1
                current_num = num
                while (current_num+1) in hs:
                    count += 1
                    current_num += 1
                ans = max(ans, count)
        return ans
        