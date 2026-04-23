# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        head = None
        tail = None
        while list1 and list2:
            node = None
            if list1.val < list2.val:
                node = list1
                list1 = list1.next
            else:
                node = list2
                list2 = list2.next
            node.next = None
            if not head:
                head = tail = node
            else:
                tail.next = node
                tail = node
        while list1:
            tail.next = list1
            tail = tail.next
            list1 = list1.next
        while list2:
            tail.next = list2
            tail = tail.next
            list2 = list2.next
        return head


        