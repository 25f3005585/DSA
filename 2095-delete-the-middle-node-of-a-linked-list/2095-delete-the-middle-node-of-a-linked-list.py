# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0

        if head.next == None:
            return head.next

        curr = head

        while curr:
            curr = curr.next
            length += 1

        middle = length // 2

        curr = head
        i = 0
        while i < middle - 1:
            i+=1
            curr = curr.next
        
        curr.next = curr.next.next
        return head