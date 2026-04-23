class Solution {
    public int longestConsecutive(int[] nums) 
    {
        if(nums.length == 0) return 0;
        Arrays.sort(nums);
        HashMap<Integer,Integer> hm = new HashMap<>();
        int ans = Integer.MIN_VALUE;
        for(int i = 0;i<nums.length;i++){
            hm.put(nums[i],hm.getOrDefault(nums[i]-1,0)+1);
            ans = Math.max(hm.get(nums[i]),ans);
        }
        return ans;
    }
}
