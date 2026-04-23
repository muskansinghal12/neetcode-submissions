class Solution {
    
    public String encode(List<String> strs) 
    {
        StringBuilder sb = new StringBuilder();
        for(int i = 0;i<strs.size();i++){
            sb.append(strs.get(i).length()).append('#').append(strs.get(i));
        }
        return sb.toString();
    }

    public List<String> decode(String str) {
        int i = 0;
        // int j = 0;
        List<String> res = new ArrayList<>();
        while(i<str.length()){
            int j = i;
            while(str.charAt(j) != '#'){
                j++;
            }
            int length = Integer.parseInt(str.substring(i,j));
            String s = str.substring(j+1,j+1+length);
            res.add(s);
            i = j+1+length;
        }
        return res;
    }
}
