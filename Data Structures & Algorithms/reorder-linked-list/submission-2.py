# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        slow = head
        fast = head.next
        print(head.val)
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        head1 = slow.next
        slow.next = None
        prev = None
        current = head1
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        # print(head1.val)
        head1 = prev
        temp = head
        new_head = None
        tail = None
        while temp:
            temp1 = temp.next
            temp.next = None
            # print(temp.val)
            if not new_head:
                new_head = temp
            else:
                tail.next = temp
            tail = temp
            temp = temp1
            if head1:
                temp2 = head1.next
                head1.next = None
                tail.next = head1
                tail = head1
                head1 = temp2
        head = new_head
            



        