class Solution {
    public int maxProduct(int[] nums) 
    {
        int prefix = 1;
        int max_product = Integer.MIN_VALUE;
        int suffix = 1;
        for(int i = 0;i<nums.length;i++){
            prefix = prefix * nums[i];
            max_product = Math.max(max_product,prefix);
            if(prefix == 0) prefix = 1;
        }
        for(int i = nums.length-1;i>=0;i--){
            suffix = suffix * nums[i];
            max_product = Math.max(max_product,suffix);
            if(suffix == 0) suffix = 1;
        }
        return max_product;
    }
}
