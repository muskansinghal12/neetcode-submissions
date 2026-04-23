class Solution {
    public int[] productExceptSelf(int[] nums) 
    {
        int n = nums.length;
        int prefix[] = new int[n];
        int suffix[] = new int[n];
        int res[] = new int[n];
        prefix[0] = nums[0];
        suffix[n-1] = nums[n-1];
        // int p = nums[0];
        // int s = nums[n-1];
        for(int i = 1;i<n;i++){
            prefix[i] = prefix[i-1]*nums[i];
            suffix[n-i-1] = suffix[n-i]*nums[n-1-i];
        }
        for(int i = 0;i<n;i++){
            if(i == 0){
                res[0] = suffix[1];
            }
            else if(i == n-1){
                res[n-1] = prefix[n-2];
            }
            else{
                res[i] = prefix[i-1] * suffix[i+1];
            }
        }
        return res;
    }
}  
