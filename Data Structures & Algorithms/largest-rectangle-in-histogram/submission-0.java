class Solution {
    public int largestRectangleArea(int[] heights) 
    {
        int n = heights.length;
        int[] nsr = new int[n];
        int[] nsl = new int[n];
        Stack<Integer> nsr_stack = new Stack<>();
        Stack<Integer> nsl_stack = new Stack<>();
        for(int i = 0;i<n;i++){
            int curr_bar = heights[i];
            while(!nsl_stack.isEmpty() && heights[nsl_stack.peek()] >= curr_bar){
                nsl_stack.pop();
            }
            nsl[i] = nsl_stack.isEmpty() ? -1: nsl_stack.peek();
            nsl_stack.push(i);
        }
        for(int i = n-1;i>=0;i--){
            int curr_bar = heights[i];
            while(!nsr_stack.isEmpty() && heights[nsr_stack.peek()] >= curr_bar){
                nsr_stack.pop();
            }
            nsr[i] = nsr_stack.isEmpty() ? n: nsr_stack.peek();
            nsr_stack.push(i);
        }
        int maxArea = 0;
        for(int i = 0;i<n;i++){
            maxArea = Math.max(maxArea,(nsr[i]-nsl[i]-1)*heights[i]);
        }
        return maxArea;
        
    }
}
