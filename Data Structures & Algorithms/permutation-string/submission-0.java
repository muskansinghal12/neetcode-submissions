class Solution {
    public boolean checkInclusion(String s1, String s2) 
    {
       
        int s2_len = s2.length();
        int s1_len = s1.length();
        char s1_array[] = s1.toCharArray();
        Arrays.sort(s1_array);
        String s1_new = new String(s1_array);
        for(int i = 0;i<=(s2_len-s1_len);i++){
            String temp = s2.substring(i,i+s1_len);
            char temp_array[] = temp.toCharArray();
            Arrays.sort(temp_array);
            
            String sorted = new String(temp_array);
            System.out.println(sorted);
            if(s1_new.equals(sorted)){
                return true;
            }
        }
        return false;
    }
}
