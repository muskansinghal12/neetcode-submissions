class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = []
        # print(intervals)
        for x, y in intervals:
            if not ans:
                ans.append([x,y])
                continue
            if x <= ans[-1][1]:
                last_x, last_y = ans.pop()
                ans.append([min(x,last_x),max(y,last_y)])
            else:
                ans.append([x,y])
        return ans
        