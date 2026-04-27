class Solution:
    def minWindow(self, s: str, t: str) -> str:

        t_map = {}
        for j,ch in enumerate(t):
            t_map[ch] = t_map.get(ch, 0) + 1
        need = len(t_map)
        have = 0
        s_map = {}
        i = 0
        j = 0
        ans_length = float('inf')
        ans = ""
        while j < len(s):
            ch = s[j]
            s_map[ch] = s_map.get(ch, 0) + 1
            if ch in t_map and s_map[ch] == t_map[ch]:
                have += 1
            while have == need:
                if (j-i+1) < ans_length:
                    ans_length = j-i+1
                    ans = s[i:j+1]
                    print(ans)
                
                if s[i] in t_map and s_map[s[i]] == t_map[s[i]]:
                    have -= 1
                s_map[s[i]] -= 1
                if s_map[s[i]] == 0:
                    del s_map[s[i]]
                i += 1
            j += 1
        return ans
                    
            
