class Solution {
    public int numDecodings(String s) 
    {
        int n = s.length();
        int dp[] = new int[n+1];
        dp[n] = 1; //empty string always have one way;
        for(int i = n-1;i>=0;i--){
            if(s.charAt(i) == '0'){
                dp[i] = 0;
                continue;
            }
            dp[i] = dp[i+1]; //single digit will always get decoded
            if(i+1 < s.length()){
                int num = Integer.parseInt(s.substring(i,i+2));
                if(num>=1 && num <=26){
                    dp[i] += dp[i+2];
                }
            }
        }
        return dp[0];
    }
}
