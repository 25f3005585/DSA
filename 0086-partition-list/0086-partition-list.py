# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        greater_curr = ListNode(200)
        greater_head = greater_curr

        less_curr = ListNode(200)
        less_head = less_curr


        curr = head

        while curr:
            if curr.val < x:
                next = curr.next
                less_curr.next = curr
                less_curr = curr
                less_curr.next = None
                curr = next
            else:
                next = curr.next
                greater_curr.next = curr
                greater_curr = curr
                greater_curr.next = None
                curr = next
        
        less_curr.next = greater_head.next
        return less_head.next