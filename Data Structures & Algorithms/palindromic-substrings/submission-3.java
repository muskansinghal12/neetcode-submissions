class Solution {
    public int countSubstrings(String s) {
        int n = s.length();
        int ans = 0;
        for(int i = 0;i<n;i++){
            int odd_count = expand(i,i,s);
            int even_count = expand(i,i+1,s);
            ans = ans + odd_count+even_count;
        }
        return ans;
    }
    public int expand(int i, int j, String s){
        int count = 0;
        while(i>=0 && j<s.length() && s.charAt(i) == s.charAt(j)){
            count++;
            i--;
            j++;
        }
        return count;
    }
}
