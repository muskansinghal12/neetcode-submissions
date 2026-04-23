class Solution:
    3#abc -> end = 1,
    def encode(self, strs: List[str]) -> str:
        encoded_string = []
        # total_length = 0
        # encoded_length = ''
        for s in strs:
            encoded_string.append(str(len(s)))
            encoded_string.append('#')
            encoded_string.append(s)
        return "".join(encoded_string)


    def decode(self, s: str) -> List[str]:
        i = 0
        ans = []
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            ans.append(s[j+1:j+length+1])
            i = j+length+1
        return ans




