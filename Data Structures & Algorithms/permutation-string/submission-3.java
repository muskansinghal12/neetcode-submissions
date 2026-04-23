class Solution {
    public boolean checkInclusion(String s1, String s2) 
    {
        int s1_length = s1.length();
        int s2_length = s2.length();
        if(s1_length>s2_length) return false;
        int freq1[] = new int[26];
        int freq2[] = new int[26];
        
        for(int i = 0;i<s1_length;i++){
            freq1[s1.charAt(i)-'a']++;
        }
        for(int i = 0;i<s1_length;i++){
            freq2[s2.charAt(i)-'a']++;
        }
        if(Arrays.equals(freq1,freq2)) return true;
        for(int i = s1_length;i<s2_length;i++){
            freq2[s2.charAt(i)-'a']++;
            freq2[s2.charAt(i-s1_length)-'a']--;
            if(Arrays.equals(freq1,freq2)) return true;
        }
        return false;
    }
}
