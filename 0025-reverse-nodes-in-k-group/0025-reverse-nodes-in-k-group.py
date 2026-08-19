# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, node):
        if node is None or node.next is None:
            return node
        head = self.reverse(node.next)
        node.next.next = node
        node.next = None
        return head

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head

        if head.next is None:
            return head

        dummyNode = ListNode(-1)
        prev = dummyNode
        curr = head

        while curr:
            start = curr
            end = curr

            i = 1
            while end and i < k:
                end = end.next
                i+=1

            if end is None:
                prev.next = start
                break

            next = end.next
            end.next = None

            nextHead = self.reverse(start)

            prev.next = nextHead
            while prev.next:
                prev = prev.next

            curr = next

        return dummyNode.next
