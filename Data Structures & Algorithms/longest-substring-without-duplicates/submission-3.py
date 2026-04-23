class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq = {}
        i = 0
        j = 0
        length = len(s)
        max_length = 0
        while j < length:
            if s[j] not in freq:
                freq[s[j]] = 0
            freq[s[j]] += 1
            if(freq[s[j]] > 1):
                index = i
                for index in range(i,j):
                    freq[s[index]] -= 1
                    i += 1
                    if s[index] == s[j]:
                        break
            max_length = max(max_length,j-i+1)
            j += 1
        return max_length
        