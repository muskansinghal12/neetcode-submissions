class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        int i = 0;
        int j = 0;
        List<Integer> l = new ArrayList<>();
        List<Integer> q = new ArrayList<>();
        while(j < nums.length){
            while(!q.isEmpty() && q.get(q.size()-1) < nums[j]){
                q.remove(q.size()-1);
            }
            q.add(nums[j]);
            if((j-i+1) < k){
                j++;
            }
            else if((j-i+1) == k){
                l.add(q.get(0));
                if(q.get(0) == nums[i]){
                    q.remove(0);
                }
                j++;
                i++;
            }
            
        }
        int ans_array[] = new int[l.size()];
        for(int index = 0;index<l.size();index++){
            ans_array[index] = l.get(index);
        }
        return ans_array;
    }
}
