class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        int i = 0;
        int j = 0;
        List<Integer> l = new ArrayList<>();
        while(j < nums.length){
            j++;
            if((j-i) == k){
                int max_element = Integer.MIN_VALUE;
                for(int index = i;index<j;index++){
                    max_element = Math.max(nums[index],max_element);
                }
                l.add(max_element);
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
