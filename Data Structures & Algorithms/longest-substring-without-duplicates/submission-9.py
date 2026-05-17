class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hs = set()
        i = 0
        j = 0
        n = len(s)
        ans = 0
        while j < n:
            ch = s[j]
            while ch in hs:
                hs.remove(s[i])
                i += 1
            ans = max(ans, j-i+1)
            hs.add(s[j])
            j += 1
        return ans
            
        