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

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = self.reverse(l1)
        l2 = self.reverse(l2)

        curr1 = l1
        curr2 = l2

        dummyNode = ListNode(-1)
        curr = dummyNode
        carry = 0

        while curr1 and curr2:
            sum_value = curr1.val + curr2.val + carry
            value = sum_value % 10
            carry = sum_value // 10

            node = ListNode(value)
            curr.next = node
            curr = node

            curr1 = curr1.next
            curr2 = curr2.next

        while curr2:
            sum_value = curr2.val + carry
            value = sum_value % 10
            carry = sum_value // 10

            node = ListNode(value)
            curr.next = node
            curr = node

            curr2 = curr2.next
        
        while curr1:
            sum_value = curr1.val + carry
            value = sum_value % 10
            carry = sum_value // 10

            node = ListNode(value)
            curr.next = node
            curr = node

            curr1 = curr1.next
        
        if carry != 0:
            node = ListNode(1)
            curr.next = node

        return self.reverse(dummyNode.next)