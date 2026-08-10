# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next is None:
            return None

        length = 0
        curr = head

        while curr:
            length += 1
            curr = curr.next

        if n == length:
            return head.next

        index = length - n
        i = 1
        curr = head
        while i < index:
            i+=1
            curr = curr.next

        curr.next = curr.next.next
        return head