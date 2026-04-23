class Solution {
    public int trap(int[] heights) {
        int n = heights.length;
        int forward[] = new int[n];
        int backward[] = new int[n];
        int water = 0;
        forward[0] = heights[0];
        for(int i = 1;i<n;i++){
            forward[i] = Math.max(forward[i-1],heights[i]);
        }
        // 0,2,2,3,3,3,3,3,3,3
        // 3,3,3,3,3,3,3,3,2,1
        backward[n-1] = heights[n-1];
        for(int i = n-2;i>=0;i--){
            
            backward[i] = Math.max(heights[i],backward[i+1]);
        }
        for(int i = 1;i<n-1;i++){
            water += Math.min(forward[i],backward[i]) - heights[i];
        }
        return water;
    }
}
