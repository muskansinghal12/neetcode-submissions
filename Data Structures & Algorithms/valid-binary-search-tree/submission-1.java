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
    public boolean isValidBST(TreeNode root) {
        List<Integer> ans = new ArrayList<>();
        isValidBSTHelper(root,ans);
        for(int i = 1;i<ans.size();i++){
            if(ans.get(i)<=ans.get(i-1)){
                return false;
            }
        }
        return true;
    }
    public void isValidBSTHelper(TreeNode root, List<Integer> inorder){
        if(root == null) return;
        isValidBSTHelper(root.left, inorder);
        inorder.add(root.val);
        isValidBSTHelper(root.right, inorder);
    }
}
