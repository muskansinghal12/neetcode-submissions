class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # char_present = set()
        freq = {}
        i = 0
        j = 0
        length = len(s)
        ans = 0
        while j < length:
            ch = s[j]
            if ch not in freq:
                freq[ch] = 0
            freq[ch] += 1
            max_freq = 0
            max_freq_char = None
            for char in freq.keys():
                if freq[char] > max_freq:
                    max_freq = freq[char]
                    max_freq_char = char
            while (j-i+1)-max_freq > k:
                freq[s[i]] -= 1
                if freq[s[i]] == 0:
                    del freq[s[i]]
                i += 1
            ans = max(ans, (j-i+1))
            j += 1
        return ans



        