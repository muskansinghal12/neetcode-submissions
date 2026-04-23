class Solution {
    public List<List<Integer>> combinationSum(int[] nums, int target) {
        List<List<Integer>> ans = new ArrayList<>();
        List<Integer> curr = new ArrayList<>();
        combinationSumHelper(nums, target, nums.length-1, curr, ans);
        return ans;
    }
    public void combinationSumHelper(int[] nums, int target, int n, List<Integer> current,List<List<Integer>> ans){
        if(target < 0 || n < 0){
            return;
        }
        if(target == 0){
            ans.add(new ArrayList<Integer>(current));
            return;
        }
        current.add(nums[n]);
        combinationSumHelper(nums,target-nums[n],n,current,ans);
        current.remove(current.size()-1);
        combinationSumHelper(nums,target,n-1,current,ans);
    }
}
