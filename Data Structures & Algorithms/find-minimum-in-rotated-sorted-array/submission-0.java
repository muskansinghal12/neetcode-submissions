class Solution {
    public int findMin(int[] nums) 
    {
        int min_value = Integer.MAX_VALUE;
        int low = 0;
        int high = nums.length-1;
        while(low <= high){
            int mid = (low+high)/2;
            if(nums[low] <= nums[mid]){
                min_value = Math.min(min_value, nums[low]);
                low = mid+1;
            }
            else{
                min_value = Math.min(min_value, nums[mid]);
                high = mid-1;
            }
        }
        return min_value;
        
    }
}
