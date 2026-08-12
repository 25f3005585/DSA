# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        dummyNode = ListNode(-1)
        dummyNode.next = head

        curr = head
        prev = dummyNode

        while curr and curr.next:
            next = curr.next.next
            prev.next = curr.next
            curr.next.next = curr
            curr.next = next
            prev = curr
            curr = next

        return dummyNode.next