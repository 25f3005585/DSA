# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        dummyNode = ListNode(-200)
        prev = dummyNode
        curr = head

        while curr and curr.next:
            if curr.val == curr.next.val:
                val = curr.val
                while curr and curr.val == val:
                    curr = curr.next
            else:
                prev.next = curr
                prev = curr
                curr = curr.next
        
        if curr:
            prev.next = curr
        else:
            prev.next = None

        return dummyNode.next