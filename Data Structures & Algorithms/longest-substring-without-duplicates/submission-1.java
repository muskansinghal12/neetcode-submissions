class Solution {
    public int lengthOfLongestSubstring(String s) 
    {
        int i = 0;
        int j = 0;
        int n = s.length();
        HashSet<Character> hs = new HashSet<>();
        int longest = 0;
        while(j < n){
            char ch = s.charAt(j);
            while(hs.contains(ch)){
                hs.remove(s.charAt(i));
                i++;
            }
            hs.add(ch);
            longest = Math.max(longest,j-i+1);
            j++;
            

        }
        return longest;
    }
}
