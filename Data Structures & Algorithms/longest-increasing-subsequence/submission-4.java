class Solution {
    public int lengthOfLIS(int[] nums) {
        int n = nums.length;
        int dp[][] = new int[n+1][n+1];
        for(int i = 0;i<=n;i++){
            Arrays.fill(dp[i],-1);
        }
        return lengthOfLISHelper(nums,nums.length,nums.length,dp);
    }
    public int lengthOfLISHelper(int[] nums, int i, int prev_index, int[][] dp){
        if(i==0) return 0;
        if(dp[i][prev_index] != -1) return dp[i][prev_index];
        int not_taken = lengthOfLISHelper(nums,i-1,prev_index,dp);
        int taken = 0;
        if(prev_index == nums.length || nums[i-1] < nums[prev_index]){
            taken = 1 + lengthOfLISHelper(nums,i-1,i-1,dp);
        }
        return dp[i][prev_index] = Math.max(taken, not_taken);
    }
}
