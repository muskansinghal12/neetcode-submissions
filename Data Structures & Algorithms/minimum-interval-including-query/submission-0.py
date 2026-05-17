class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        ans = []
        for query in queries:
            current_ans = float('inf')
            for x,y in intervals:
                if x<=query and query<=y:
                    current_ans = min(current_ans, y-x+1)
            ans.append(-1 if current_ans == float('inf') else current_ans)
        return ans

        