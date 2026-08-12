# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None or head.next.next is None:
            return head

        odd = head
        even = head.next
        evenHead = head.next

        dummyNode = ListNode(-1)
        dummyNode.next = head

        while even and even.next:
            oddnext = odd.next.next
            odd.next = oddnext
            odd = oddnext

            evennext = even.next.next
            even.next = evennext
            even = evennext

        odd.next = evenHead

        return dummyNode.next
        
