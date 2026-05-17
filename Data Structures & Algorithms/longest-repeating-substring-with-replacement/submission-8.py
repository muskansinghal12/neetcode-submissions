class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        i = 0
        j = 0
        n = len(s)
        ans = 0
        max_freq = 0
        while j < n:
            freq[s[j]] = freq.get(s[j],0) + 1
            max_freq = max(max_freq, freq[s[j]])
            while (j-i+1)-max_freq > k:
                freq[s[i]] -= 1
                i += 1
            ans = max(ans, j-i+1)
            j += 1
        return ans

        