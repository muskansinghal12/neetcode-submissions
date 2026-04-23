/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    int maxSum = Integer.MIN_VALUE;
    public int maxPathSum(TreeNode root) {
        maxPathSumHelper(root);
        return maxSum;
    }
    public int maxPathSumHelper(TreeNode root) {
        if(root == null) return 0;

        int left = maxPathSumHelper(root.left);
        int right = maxPathSumHelper(root.right);
        int converged_path = left+ right +root.val;
        int left_or_right = Math.max(left, right) + root.val;
        int only_root = root.val;
        maxSum = Math.max(maxSum,Math.max(converged_path,Math.max(left_or_right,only_root)));
        return Math.max(left_or_right,only_root);
        
    }
}
