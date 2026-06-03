import heapq
class Solution:
    def helper(self, root, k):
        if root is None:
            return
        self.helper(root.left, k)
        heapq.heappush(self.pq, -root.val)
        if len(self.pq) > k:
            heapq.heappop(self.pq)
        self.helper(root.right, k)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.pq = []
        self.helper(root, k)
        return -self.pq[0]