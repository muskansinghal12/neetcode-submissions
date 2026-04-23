class Solution {
    public boolean wordBreak(String s, List<String> wordDict) {
        HashSet<String> hs = new HashSet<>();
        int n = s.length();
        Boolean memo[] = new Boolean[n];
        for(String str : wordDict){
            hs.add(str);
        }
        return wordBreakHelper(s,hs,0,memo);
    }
    public boolean wordBreakHelper(String s, HashSet<String> hs, int i, Boolean memo[]){
        if(i==s.length()) return true;
        if(memo[i] != null) return memo[i];
        for(int k = i;k<s.length();k++){
            if(hs.contains(s.substring(i,k+1)) && wordBreakHelper(s,hs,k+1,memo)){
                return memo[i] = true;
            }
        }
        return memo[i] = false;
    }
}
