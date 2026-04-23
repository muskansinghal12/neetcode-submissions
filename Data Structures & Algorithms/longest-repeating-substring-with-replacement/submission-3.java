class Solution {
    public int characterReplacement(String s, int k) 
    {
        int i = 0;
        int j = 0;
        int n = s.length();
        int[] freq = new int[26];
        int longest = 0;
        int max_freq = 0;
        while(j<n){
            char ch = s.charAt(j);
            freq[ch-'A']++;
            max_freq = Math.max(max_freq,freq[ch-'A']);
            while((j-i+1)-max_freq > k) {
                freq[s.charAt(i)-'A']--;
                i++;
            }
            longest = Math.max(longest, j-i+1); 
            j++;
        }
        return longest;
    }
}
