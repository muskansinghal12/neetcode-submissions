# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        queue = deque()
        if root is not None:
            queue.append(root)
        while queue:
            length = len(queue)
            level = []
            for _ in range(length):
                current = queue.popleft()
                level.append(current.val)
                if current.left is not None:
                    queue.append(current.left)
                if current.right is not None:
                    queue.append(current.right)
            ans.append(level)
        return ans

        