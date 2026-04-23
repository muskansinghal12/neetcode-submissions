class Solution {
    public int maxArea(int[] heights) {
        int n = heights.length;
        int left = 0;
        int right = n-1;
        int maxArea = 0;
        while(left < right){
            int height = Math.min(heights[right],heights[left]);
            int width = right-left;
            maxArea = Math.max(maxArea,height*width);
            if(heights[left] < heights[right])left++;
            else right--;
        }
        return maxArea;
    }
}
