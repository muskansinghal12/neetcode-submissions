# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def helper(self, preorder, inorder, start, end):
        if end < start:
            return None
        i = 0
        for j in range(start, end+1):
            if inorder[j] == preorder[self.index]:
                i = j
                break
        
        root = TreeNode(preorder[self.index],None,None)
        self.index += 1
        root.left = self.helper(preorder, inorder, start, i-1)
        root.right = self.helper(preorder, inorder, i+1, end)
        return root


    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.index = 0
        return self.helper(preorder, inorder, 0, len(preorder)-1)

        