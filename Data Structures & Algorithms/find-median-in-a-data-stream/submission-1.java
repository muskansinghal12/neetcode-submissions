class MedianFinder {
    PriorityQueue<Integer> first_half;
    PriorityQueue<Integer> last_half;
    public MedianFinder() {
        first_half = new PriorityQueue<>((a,b) -> b-a); //more elements
        last_half = new PriorityQueue<>((a,b) -> a-b);
    }
    
    public void addNum(int num) {
        first_half.add(num);
        if(!last_half.isEmpty() && first_half.peek() > last_half.peek())
            last_half.add(first_half.poll());

        if(first_half.size() > last_half.size()+1){
            last_half.add(first_half.poll());
        }
        else if(last_half.size() > first_half.size()){
            first_half.add(last_half.poll());
        }
    }
    
    public double findMedian() {
        int first_size = first_half.size();
        int last_size = last_half.size();
        if((first_size+last_size)%2 == 0){
            int first = first_half.peek();
            int second = last_half.peek();
            return (first+second)/2.0;
        }
        else{
            return first_half.peek()/1.0;
        }
    }
}
