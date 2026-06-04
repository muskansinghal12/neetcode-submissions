# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def helper(self, root):
        if root is None:
            return 0
        left_sum = self.helper(root.left)
        right_sum = self.helper(root.right)
        both_good_sum = left_sum + right_sum + root.val
        only_one_good_sum = max(left_sum, right_sum)+ root.val
        only_root = root.val
        self.maxSum = max(max(self.maxSum,both_good_sum), max(only_one_good_sum,only_root))
        return max(only_one_good_sum,only_root)
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxSum = float('-inf')
        self.helper(root)
        return self.maxSum
        
        