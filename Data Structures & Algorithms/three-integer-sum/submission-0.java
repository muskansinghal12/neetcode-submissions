class Solution {
    public List<List<Integer>> threeSum(int[] nums) 
    {
        HashSet<List<Integer>> ans = new HashSet<>();
        Arrays.sort(nums);
        for(int i = 0;i<nums.length;i++){
            int j = i+1;
            int k = nums.length-1;
            while(j<k){
                if(nums[j]+nums[k] == -nums[i]){
                    List<Integer> l = new ArrayList<>();
                    l.add(nums[i]);
                    l.add(nums[j]);
                    l.add(nums[k]);
                    ans.add(l);
                    j++;
                    k--;
                }
                else if(nums[j]+nums[k] < -nums[i]){
                    j++;
                }
                else{
                    k--;
                }
            }

        }

        return new ArrayList<>(ans);
    }
}
