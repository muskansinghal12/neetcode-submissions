/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode mergeKLists(ListNode[] lists) 
    {
        PriorityQueue<ListNode> pq = new PriorityQueue<>((a,b) -> a.val-b.val);
        for(int i = 0;i<lists.length;i++){
            ListNode head = lists[i];
            while(head != null){
                ListNode temp = head;
                head = head.next;
                temp.next = null;
                pq.add(temp);
            }
        }
        System.out.println(pq.size());
        ListNode head = null;
        ListNode tail = null;
        while(!pq.isEmpty()){
            ListNode node = pq.poll();
            if(head == null){
                head = node;
            }
            else{
                tail.next = node;
            }
            tail = node;
        }
        return head;
    }
}
