class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = []
        s = s.lower()
        for i in range(len(s)):
            if s[i].isalnum():
                clean_s.append(s[i])
        clean_s = ''.join(clean_s)
        i = 0
        j = len(clean_s)-1
        while i < j:
            if clean_s[i] != clean_s[j]:
                return False
            i += 1
            j -= 1
        return True



        