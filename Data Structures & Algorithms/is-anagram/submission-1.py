class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freq = [0]*26
        length = len(s)
        for i in range(length):
            freq[ord(s[i])-ord('a')] = freq[ord(s[i])-ord('a')] +  1
            freq[ord(t[i])-ord('a')] = freq[ord(t[i])-ord('a')] - 1
        for i in range(26):
            if freq[i] != 0:
                return False
        return True        