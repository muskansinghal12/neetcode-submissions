class Solution {
    public int lengthOfLIS(int[] nums) {
        return lengthOfLISHelper(nums,nums.length,-1);
    }
    public int lengthOfLISHelper(int[] nums, int i, int prev){
        if(i==0) return 0;
        int not_taken = lengthOfLISHelper(nums,i-1,prev);
        int taken = 0;
        if(prev == -1 || nums[i-1] < prev){
            taken = 1 + lengthOfLISHelper(nums,i-1,nums[i-1]);
        }
        return Math.max(taken, not_taken);
    }
}
