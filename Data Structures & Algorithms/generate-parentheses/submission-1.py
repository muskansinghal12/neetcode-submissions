class Solution:
    def helper(self, n, ans, opened, closed, current_set):
        if len(current_set) == 2*n:
            ans.append("".join(current_set))
            return
        if opened < n:
            current_set.append("(")
            self.helper(n,ans, opened+1,closed,current_set)
            current_set.pop()
        if closed < opened:
            current_set.append(")")
            self.helper(n,ans, opened,closed+1,current_set)
            current_set.pop()
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        self.helper(n,ans,0,0,[])
        return ans