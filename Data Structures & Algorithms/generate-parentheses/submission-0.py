class Solution:
    def helper(self, n, ans, opened, closed, current_set):
        if opened > n or closed > n or closed > opened:
            return
        if opened == n and closed == n:
            ans.append("".join(current_set))
            return
        current_set.append("(")
        self.helper(n,ans, opened+1,closed,current_set)
        current_set.pop()
        current_set.append(")")
        self.helper(n,ans, opened,closed+1,current_set)
        current_set.pop()
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        self.helper(n,ans,0,0,[])
        return ans