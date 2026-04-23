class Solution {
    public int minEatingSpeed(int[] piles, int h) 
    {
        int low = 1;
        int high = 0;
        int n = piles.length;
        int ans = 0;
        for(int i = 0;i<n;i++){
            high = Math.max(high,piles[i]);
        }
        while(low <= high){
            int mid = low+(high-low)/2;
            int hrs = calculateHours(piles,mid);
            if(hrs <= h){
                ans = mid;
                high = mid-1;
            }
            else{
                low = mid+1;
            }
        }
        return ans;
    }
    public int calculateHours(int[] piles, int k){
        int hrs = 0;
        for(int i = 0;i<piles.length;i++){
            hrs += (piles[i]+k-1)/k;
        }
        // System.out.println(hrs);
        return hrs;
    }
}
