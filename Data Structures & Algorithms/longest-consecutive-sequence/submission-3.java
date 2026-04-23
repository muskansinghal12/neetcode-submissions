class Solution {
    public int longestConsecutive(int[] nums) 
    {
        if(nums.length == 0) return 0;
        // Arrays.sort(nums);
        HashSet<Integer> hs = new HashSet<>();
        int ans = Integer.MIN_VALUE;
        int longest = 1;
        for(int i = 0;i<nums.length;i++){
            hs.add(nums[i]);
        }
        for(int num : hs){
            int count = 1;
            int current_num = num;
            
            if(!hs.contains(current_num-1)){
                while(hs.contains(current_num+1)){
                    current_num++;
                    count++;
                }
                longest = Math.max(longest,count);
            }
        }
        return longest;
    }
}
