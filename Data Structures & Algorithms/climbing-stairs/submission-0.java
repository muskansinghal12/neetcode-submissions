class Solution {
    public int climbStairs(int n) 
    {
        if(n == 1 || n == 2) return n;
        int n_1 = 1;
        int n_2 = 2;
        for(int i = 2;i<n;i++){
            int temp = n_1+n_2;
            n_1 = n_2;
            n_2 = temp;
        }
        return  n_2;
    }
}
