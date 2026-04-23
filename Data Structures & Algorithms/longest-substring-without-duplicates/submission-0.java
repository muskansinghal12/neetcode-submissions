class Solution {
    public int lengthOfLongestSubstring(String s) 
    {
        int i = 0;
        int j = 0;
        int n = s.length();
        HashSet<Character> hs = new HashSet<>();
        int longest = 0;
        while(j < n){
            if(hs.contains(s.charAt(j))){
                while(s.charAt(i)!=s.charAt(j))
                {
                    hs.remove(s.charAt(i));
                    i++;
                }
                i++;

            }
            hs.add(s.charAt(j));
            j++;
            longest = Math.max(longest,j-i);
            

        }
        return longest;
    }
}
