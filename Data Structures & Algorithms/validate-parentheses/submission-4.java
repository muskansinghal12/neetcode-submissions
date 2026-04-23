class Solution {
    public boolean isValid(String s) 
    {
        if(s.length()%2 != 0) return false;
        HashMap<Character,Character> hm = new HashMap<>();
        hm.put(')','(');
        hm.put('}','{');
        hm.put(']','[');
        Stack<Character> st = new Stack<>();
        for(int i = 0;i<s.length();i++){
            char ch = s.charAt(i);
            if(ch == '(' || ch == '{' || ch == '['){
                st.push(ch);
            }
            else{
                char open = hm.get(ch);
                if(!st.isEmpty() && st.peek() == open){
                    st.pop();
                }
                else{
                    return false;
                }
            }
        }
        return st.isEmpty();

        
    }
}
