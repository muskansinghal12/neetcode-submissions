import sys
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        t_freq = Counter(t)
        i = 0
        j = 0
        required = len(t_freq)
        formed = 0
        window = {}
        ans = [sys.maxsize,-1,-1]
        while j < len(s):
            ch = s[j]
            if ch not in window:
                window[ch] = 0
            window[ch] += 1
            if ch in window and window[ch] == t_freq[ch]:
                formed += 1
            while required == formed:
                if (j-i+1) < ans[0]:
                    ans = [(j-i+1),i,j]
                if s[i] in t_freq and window[s[i]] == t_freq[s[i]]:
                    formed -= 1
                window[s[i]] -= 1
                if window[s[i]] == 0:
                    del window[s[i]]
                i += 1
            j += 1
        return "" if ans[0] == sys.maxsize else s[ans[1]:ans[2]+1]

         