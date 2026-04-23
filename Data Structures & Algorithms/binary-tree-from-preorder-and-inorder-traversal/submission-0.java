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
    int pre_index = 0;
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        return buildTreeHelper(preorder,inorder,0,inorder.length-1);
    }
    public TreeNode buildTreeHelper(int[] preorder, int[] inorder,
    int in_start, int in_end){
        if(in_start > in_end) return null;
        int index = -1;
        for(int i = in_start;i<=in_end;i++){
            if(preorder[pre_index] == inorder[i]){
                index = i;
                break;
            }
        }
        TreeNode root = new TreeNode(preorder[pre_index++]);
        root.left = buildTreeHelper(preorder,inorder,in_start,index-1);
        root.right = buildTreeHelper(preorder,inorder,index+1,in_end);
        return root;
    }
}
