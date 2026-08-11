# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     previous = None
    #     current = head

    #     while current:
    #         next = current.next
    #         current.next = previous
    #         previous = current
    #         current = next
        
    #     return previous

    def recursive_reverse(self,node):
            if node == None or node.next == None:
                return node
            
            newHead = self.recursive_reverse(node.next)
            node.next.next = node
            node.next = None
            return newHead

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.recursive_reverse(head)