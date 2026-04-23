class Solution {
    public int characterReplacement(String s, int k) 
    {
        int i = 0;
        int j = 0;
        int n = s.length();
        int[] freq = new int[26];
        int longest = 0;
        while(j<n){
            char ch = s.charAt(j);
            freq[ch-'A']++;
            int max_freq = 0;
            char max_ch;
            for(int m = i;m<=j;m++){
                if(freq[s.charAt(m)-'A'] > max_freq){
                    max_ch = s.charAt(m);
                    max_freq = freq[s.charAt(m)-'A'];
                }
            }
            if((j-i+1)-max_freq <= k) {
                longest = Math.max(longest, j-i+1); 
            }
            else{
                freq[s.charAt(i)-'A']--;
                i++;
            }
            j++;
        }
        return longest;
    }
}
