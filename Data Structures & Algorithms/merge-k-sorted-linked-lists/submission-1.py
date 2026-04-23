import heapq
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pq = []
        count = 0
        for l in lists:
            temp = l
            while temp is not None:
                heapq.heappush(pq,(temp.val,count,temp))
                temp = temp.next
                count += 1 #to avoid the comparison of two listnode when values are same
            
        head = None
        tail = None
        while pq:
            priority,count, node = heapq.heappop(pq)
            node.next = None
            if head is None:
                head = node
            else:
                tail.next = node
            tail = node
        return head

        