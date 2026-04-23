class Solution {
    public int numDecodings(String s) 
    {
        
        return numDecodingsHelper(s,0);
    }
    public int numDecodingsHelper(String s, int i){
         if(i == s.length()) return 1;
         if(s.charAt(i) == '0') return 0;
         int one = numDecodingsHelper(s,i+1);
         int two = 0;
         if(i+1 < s.length()){
            int val = Integer.parseInt(s.substring(i,i+2));
            if(val>=1 && val <= 26){
                two = numDecodingsHelper(s,i+2);
            }
            
         }
        return one+two;
    }
}
