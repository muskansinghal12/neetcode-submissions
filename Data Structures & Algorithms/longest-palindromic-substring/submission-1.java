class Solution {
    public String longestPalindrome(String s) {
        int n = s.length();
        String ans = "";
        int ans_length = 0;
        for(int i = 0;i<n;i++){
            String odd = expand(i,i,s);
            String even = expand(i,i+1,s);
            if(odd.length() > ans_length){
                ans = odd;
                ans_length = odd.length();
            }
            if(even.length() > ans_length){
                ans = even;
                ans_length = even.length();
            }

        }
        return ans;
    }
    public String expand(int i, int j, String s){
        String ans = "";
        while(i>=0 && j<s.length() && s.charAt(i) == s.charAt(j)){
            ans = s.substring(i,j+1);
            i--;
            j++;
        }
        return ans;
    }
}
