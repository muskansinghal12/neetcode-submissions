# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    count = 0
    path = []
    def helper(self, root):
        if root is None:
            return
        self.path.append(root)
        flag = True
        for element in self.path:
            if element.val > root.val:
                flag = False 
                break
        if flag:
            self.count += 1
        self.helper(root.left)
        self.helper(root.right)
        self.path.pop()

    def goodNodes(self, root: TreeNode) -> int:
        self.helper(root)
        return self.count
        
        