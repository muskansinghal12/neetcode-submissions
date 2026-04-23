class Solution {
    public int evalRPN(String[] tokens) 
    {
        Stack<Integer> st = new Stack<>();
        for(int i = 0;i<tokens.length;i++){
            String ch = tokens[i];
            if(ch.equals("+") || ch.equals("-") || ch.equals("*") || ch.equals("/")){
                
                int second = st.pop();
                int first = st.pop();
                int ans = perform_operation(first, second,ch);
                st.push(ans);
            }
            else{
                st.push(Integer.parseInt(tokens[i]));
            }
        }
        return st.peek();
    }
    public int perform_operation(int first, int second, String opr){
        switch(opr){
            case "+":
                return first+second;
            case "-":
                return first-second;
            case "*":
                return first*second;
            case "/":
                if(second == 0) return 0;
                return first/second;
        }
        return -1;
    }
}
