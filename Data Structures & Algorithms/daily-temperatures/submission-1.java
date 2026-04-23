class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        Stack<int[]> st = new Stack<>(); //(temp, index)
        int n = temperatures.length;
        int[] ans = new int[n];
        for(int i = n-1;i>=0;i--){
            int count = 0;
            while(!st.isEmpty() && st.peek()[0] <= temperatures[i]){
                st.pop();
            }
            
            ans[i] = !st.isEmpty() ? st.peek()[1]-i : 0;
            st.push(new int[]{temperatures[i],i});
        }
        return ans;
    }
}
