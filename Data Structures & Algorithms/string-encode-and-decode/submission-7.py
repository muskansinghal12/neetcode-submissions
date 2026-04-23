class Solution:
    3#abc -> end = 1,
    def encode(self, strs: List[str]) -> str:
        encoded_string = ''
        # total_length = 0
        # encoded_length = ''
        for s in strs:
            encoded_string = encoded_string + str(len(s))
            encoded_string = encoded_string + '#'
            encoded_string = encoded_string + s
        return encoded_string


    def decode(self, s: str) -> List[str]:
        start = 0
        end = 0
        ans = []
        while end < len(s):
            if s[end] == '#':
                length = int(s[start:end])
                ans.append(s[end+1:end+length+1])
                start = end+length+1
                end = end+length+1
            else:
                end += 1
        return ans




