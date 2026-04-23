class Solution {
    public List<List<Integer>> combinationSum(int[] nums, int target) {
        Arrays.sort(nums);
        List<List<Integer>> ans = new ArrayList<>();
        List<Integer> curr = new ArrayList<>();
        combinationSumHelper(nums, target, 0, curr, ans);
        return ans;
    }
    public void combinationSumHelper(int[] nums, int target, int index, List<Integer> current,List<List<Integer>> ans){
        if(target == 0){
            ans.add(new ArrayList<Integer>(current));
            return;
        }
        for(int i = index;i<nums.length && nums[i] <= target;i++){
            current.add(nums[i]);
            combinationSumHelper(nums,target-nums[i],i,current,ans);
            current.remove(current.size()-1);
        }
    }
}
