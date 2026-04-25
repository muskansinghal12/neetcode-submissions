class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_map = {}
        for ch in t:
            if ch not in t_map:
                t_map[ch] = 0
            t_map[ch] += 1

        j = 0
        s_map = {}
        i = 0
        ans_len = float('inf')
        ans = ""
        while j < len(s):
            ch = s[j]
            if ch not in s_map:
                s_map[ch] = 0
            s_map[ch] += 1
            while i <= j:
                possible = True
                for ch,freq in t_map.items():
                    if ch not in s_map or s_map[ch] < freq:
                        possible = False
                        break
                if possible:
                    if j-i+1 < ans_len:
                        ans = s[i:j+1]
                        ans_len = j-i+1
                    s_map[s[i]] -= 1
                    i += 1
                else:
                    break

            j += 1
        return ans
               