class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ''
        for s in strs:
            ans = ans + str(len(s)) + '#' + s
        # print(ans)
        return ans


    def decode(self, s: str) -> List[str]:
        length = len(s)
        i = 0
        ans = []
        while i < length:

            word_len = 0
            while s[i] != '#':
                word_len = word_len*10 +  (ord(s[i]) - ord('0'))
                i += 1
            i += 1 #to escape #
            ans.append(s[i:i+word_len])
            i = i+word_len
        return ans
             

