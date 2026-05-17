class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_freq = {}
        s_freq = {}
        # need = 0
        for ch in t: 
            t_freq[ch] = t_freq.get(ch,0) + 1
        # for i in range(26):
        #     if t_freq[i] != 0:
        #         need += 1
        i = 0
        j = 0
        n = len(s)
        need = 0
        required = len(t_freq)
        ans = float('inf')
        ans_str = ""
        while j < n:
            ch = s[j]
            s_freq[ch] = s_freq.get(ch,0) + 1
            if ch in t_freq and s_freq[ch] == t_freq[ch]:
                need += 1
            while need == required:
                if (j-i+1) < ans:
                    ans = j-i+1
                    ans_str = s[i:j+1]
                
                if s[i] in t_freq and s_freq[s[i]] == t_freq[s[i]]:
                    need -= 1
                s_freq[s[i]] -= 1
                if s_freq[s[i]] == 0:
                    del s_freq[s[i]]
                i += 1
            j += 1
        return ans_str
                




        