# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lengA = 0
        lengB = 0

        curr = headA

        while curr:
            lengA+=1
            curr = curr.next
        
        curr = headB

        while curr:
            lengB+=1
            curr = curr.next

        currA = headA
        currB = headB
        
        while lengA > lengB:
            lengA -= 1
            currA = currA.next

        while lengB > lengA:
            lengB -= 1
            currB = currB.next

        
        while currA and currB:
            if currA == currB:
                return currA
            
            currA = currA.next
            currB = currB.next

        return None
        

