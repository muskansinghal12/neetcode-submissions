class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {ch:i for i, ch in enumerate(s)}
        start = 0
        end = 0
        ans = []
        for i, ch in enumerate(s):
            end = max(end, last[ch])
            if i == end:
                ans.append(end-start+1)
                start = end+1
        return ans
        