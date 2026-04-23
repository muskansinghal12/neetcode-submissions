class Car implements Comparable<Car>{
    public int position;
    public int speed;
    public Car(int position, int speed){
        this.position = position;
        this.speed = speed;
    }
    public int compareTo(Car o){
        return this.position-o.position;
    }
}
class Solution {
    public int carFleet(int target, int[] position, int[] speed) {
        int n = position.length;
        List<Car> cars = new ArrayList<>();
        for(int i = 0;i<n;i++){
            cars.add(new Car(position[i],speed[i]));
        }
        Collections.sort(cars);
        Stack<Double> st = new Stack<>();
        for(int i = n-1;i>=0;i--){
            double time = (target-cars.get(i).position)/(double)cars.get(i).speed;
            
            if(!st.isEmpty() && time <= st.peek()){
                continue;
            }
            st.push(time);
        }
        return st.size();
    }
}
