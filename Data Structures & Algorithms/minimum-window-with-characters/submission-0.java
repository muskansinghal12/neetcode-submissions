class Solution {
    public String minWindow(String s, String t) 
    {
        HashMap<Character,Integer> hm = new HashMap<>();
        int ans_length = Integer.MAX_VALUE;
        String ans = "";
        int count = t.length();
        for(int i = 0;i<t.length();i++){
            hm.put(t.charAt(i),hm.getOrDefault(t.charAt(i),0)+1);
        }
        int i = 0;
        int j = 0;
        while(j < s.length()){
            char ch = s.charAt(j);
            if(hm.containsKey(ch)){
                hm.put(ch, hm.get(ch)-1);
                if(hm.get(ch) >= 0){
                    count--;
                }
            }
            while(count == 0){
                if((j-i+1) < ans_length){
                    ans_length = j-i+1;
                    ans = s.substring(i,j+1);
                }
                char left = s.charAt(i);
                if(hm.containsKey(left)){
                    hm.put(left, hm.get(left)+1);
                    if(hm.get(left) > 0){
                        count++;
                    }
                }
                i++;
            }
            j++;
        }
        return ans;
    }
}
