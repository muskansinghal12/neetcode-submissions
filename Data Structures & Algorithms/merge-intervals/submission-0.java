class Solution {
    public int[][] merge(int[][] intervals) {
        Arrays.sort(intervals,(a,b) -> a[0]-b[0]);
        List<int[]> ans = new ArrayList<>();
        int i = 1;
        ans.add(intervals[0]);
        int n = intervals.length;
        while(i<n){
            int last[] = ans.get(ans.size()-1);
            if(last[1] >= intervals[i][0]){
                int first = Math.min(last[0],intervals[i][0]);
                int second = Math.max(last[1],intervals[i][1]);
                ans.remove(ans.size()-1);
                ans.add(new int[]{first,second});
            }
            else{
                ans.add(intervals[i]);
            }
            i++;
        }
        return ans.toArray(new int[ans.size()][]);
    }
}
