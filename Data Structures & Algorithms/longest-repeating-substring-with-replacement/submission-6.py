class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = 0
        hm = {}
        max_freq = 0
        ans = 0
        for j,ch in enumerate(s):
            if ch in hm:
                hm[ch] += 1
            else:
                hm[ch] = 1
            max_freq = max(max_freq,hm[ch])
            while (j-i+1)-max_freq > k:
                hm[s[i]] -= 1
                i += 1
            ans = max(ans, j-i+1)
            j += 1
        return ans
            

        