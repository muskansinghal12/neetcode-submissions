class MinStack {
    Stack<Long> st;
    long min_element = Long.MAX_VALUE;
    public MinStack() {
        st = new Stack<>();
    }
    
    public void push(int val) {
        long value = (long)val;
        if(st.isEmpty()){
            st.push(value);
            min_element = value;
        }
        else{
            if(value < min_element){
                st.push(2*value-min_element);
                min_element = value;
            }
            else{
                st.push(value);
            }
        }
    }
    
    public void pop() {
        if(!st.isEmpty()){
            long top = st.peek();
            if(top < min_element){
                min_element = 2*min_element - top;
            }
            st.pop();
        }
    }
    
    public int top() {
        if(!st.isEmpty()){
            long top = st.peek();
            if(top < min_element){
                return (int)min_element;
            }
            else{
                return (int)top;
            }
        }
        return -1;
    }
    
    public int getMin() {
        if (st.isEmpty()) return -1;   // or throw exception
        return (int)min_element;
    }
}
