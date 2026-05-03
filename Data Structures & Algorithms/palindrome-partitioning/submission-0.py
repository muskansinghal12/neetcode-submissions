class Solution:
    def isPalindrome(self, i, j, s):
        while i<=j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
    def helper(self, i, s,current_ans,ans):
        if i>=len(s):
            ans.append(current_ans[:])
            return 
        for k in range(i,len(s)):
            if self.isPalindrome(i,k,s):
                # print(s[i:k+1])
                current_ans.append(s[i:k+1])
                self.helper(k+1,s,current_ans,ans)
                current_ans.pop()



    def partition(self, s: str) -> List[List[str]]:
        ans = []
        n = len(s)
        self.helper(0,s,[],ans)
        return ans

        