class Solution:
    def helper(self, digits, i, current_set, ans, mapping):
        if i == len(digits):
            if len(current_set) > 0:
                ans.append("".join(current_set))
            return
        for ch in mapping[digits[i]]:
            current_set.append(ch)
            self.helper(digits,i+1,current_set,ans, mapping)
            current_set.pop()
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        ans = []
        self.helper(digits,0,[],ans,mapping)
        return ans
        