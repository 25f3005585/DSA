# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode(200)
        curr = dummyNode
        
        curr1 = list1
        curr2 = list2

        while curr1 and curr2:
            if curr1.val <= curr2.val:
                node = ListNode(curr1.val)
                curr.next = node
                curr = node
                curr1 = curr1.next
            else:
                node = ListNode(curr2.val)
                curr.next = node
                curr = node
                curr2 = curr2.next
        
        while curr1:
            node = ListNode(curr1.val)
            curr.next = node
            curr = node
            curr1 = curr1.next
        
        while curr2:
            node = ListNode(curr2.val)
            curr.next = node
            curr = node
            curr2 = curr2.next
        
        return dummyNode.next