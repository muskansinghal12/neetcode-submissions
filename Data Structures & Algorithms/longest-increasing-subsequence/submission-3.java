class Solution {
    public int lengthOfLIS(int[] nums) {
        return lengthOfLISHelper(nums,nums.length,nums.length);
    }
    public int lengthOfLISHelper(int[] nums, int i, int prev_index){
        if(i==0) return 0;
        int not_taken = lengthOfLISHelper(nums,i-1,prev_index);
        int taken = 0;
        if(prev_index == nums.length || nums[i-1] < nums[prev_index]){
            taken = 1 + lengthOfLISHelper(nums,i-1,i-1);
        }
        return Math.max(taken, not_taken);
    }
}
