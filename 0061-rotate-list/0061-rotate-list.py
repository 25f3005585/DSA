# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        if k == 0:
            return head

        curr = head
        n = 0

        while curr:
            curr = curr.next
            n += 1
        
        k = k % n

        if k == 0:
            return head
        
        dummyNode = ListNode(200)

        index = n - k
        i = 1

        curr = head

        while i < index:
            i+=1
            curr = curr.next
        
        dummyNode.next = curr.next
        second = curr.next
        curr.next = None

        while second.next:
            second = second.next
        
        second.next = head

        return dummyNode.next