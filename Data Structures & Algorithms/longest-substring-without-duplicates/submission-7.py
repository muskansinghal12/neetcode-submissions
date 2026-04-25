class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = {}
        i = 0
        ans = 0
        for j, ch in enumerate(s):
            if ch in window and window[ch] >= i:
                i = window[ch] + 1
            window[ch] = j
            ans = max(ans, j-i+1)
        return ans
        