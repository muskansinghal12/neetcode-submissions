class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hs = set(nums)
        ans = 0
        for i in nums:
            
            if (i-1) not in hs:
                count = 1
                current_num = i
                while (current_num+1) in hs:
                    count += 1
                    current_num += 1
                ans = max(count, ans)
        return ans


        