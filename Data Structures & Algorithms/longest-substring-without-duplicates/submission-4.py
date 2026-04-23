class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last = {}
        i = 0
        ans = 0
        for j, ch in enumerate(s):
            if ch in last and last[ch] >= i:
                i = last[ch] + 1
            last[ch] = j
            ans = max(ans, j - i + 1)
        return ans