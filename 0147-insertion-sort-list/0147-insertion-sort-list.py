# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:
            return head

        dummyNode = ListNode(-5001)
        dummyNode.next = head
        curr = head.next
        head.next = None

        while curr:
            tempHead = dummyNode
            while tempHead and tempHead.next and tempHead.next.val <= curr.val:
                tempHead = tempHead.next
            
            curr_next = curr.next
            next = tempHead.next
            tempHead.next = curr
            tempHead = curr
            tempHead.next = next
            curr = curr_next
        
        return dummyNode.next