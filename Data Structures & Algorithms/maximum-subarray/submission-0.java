class Solution {
    public int maxSubArray(int[] nums) 
    {
        
        int prefix_sum = 0;
        int max_sum = Integer.MIN_VALUE;
        for(int i = 0;i<nums.length;i++){
            prefix_sum += nums[i];
            max_sum  = Math.max(prefix_sum, max_sum);
            if(prefix_sum < 0){
                prefix_sum = 0;
            }
        }
        return max_sum;
    }
}
