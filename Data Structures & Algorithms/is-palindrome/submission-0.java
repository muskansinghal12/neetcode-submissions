class Solution {
    public boolean isPalindrome(String s) 
    {
        String new_s = s.toLowerCase();
        int i = 0;
        int j = new_s.length()-1;
        while(i<j){
            char first = new_s.charAt(i);
            char last = new_s.charAt(j);
            if(!Character.isLetterOrDigit(first)){
                i++;
                continue;
            }
            if(!Character.isLetterOrDigit(last)){
                j--;
                continue;
            }
            if(first != last){
                return false;
            }
            i++;
            j--;
        }
        return true;
    }
}
