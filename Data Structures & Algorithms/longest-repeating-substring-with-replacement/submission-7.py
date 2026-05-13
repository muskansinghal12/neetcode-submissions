class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hm = {}
        i = 0
        j = 0
        ans = 0
        max_freq = 0
        while j < len(s):
            hm[s[j]] = hm.get(s[j],0) + 1
            max_freq = max(max_freq, hm[s[j]])
            while (j-i+1) - max_freq > k:
                hm[s[i]] -= 1
                i += 1
            ans = max(ans, j-i+1)
            j += 1
        return ans


        