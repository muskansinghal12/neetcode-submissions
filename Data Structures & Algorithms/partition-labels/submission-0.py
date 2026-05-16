class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ranges = {}
        for ch in s:
            ranges[ch] = [s.index(ch),s.rindex(ch)]
        intervals = sorted(ranges.values())
        ans = []
        
        for x,y in intervals:
            if not ans or ans[-1][1] < x:
                ans.append([x,y])
            else:
                ans[-1][1] = max(ans[-1][1],y)
        res = []
        for x,y in ans: 
            res.append(y-x+1)
        return res

        