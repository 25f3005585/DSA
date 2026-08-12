# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self,node):
        if node is None or node.next is None:
            return node

        newhead = self.reverse(node.next)
        node.next.next = node
        node.next = None
        return newhead

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        isOdd = False

        if fast is not None:
            isOdd = True
        
        if isOdd:
            slow = slow.next

        first = head
        second = self.reverse(slow)

        while second:
            if first.val != second.val:
                return False

            first = first.next
            second = second.next
        
        return True