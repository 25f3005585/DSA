# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
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

        while curr1:
            sum_value = curr1.val + carry
            value = sum_value % 10
            carry = sum_value // 10

            node = ListNode(value)
            curr.next = node
            curr = node
            curr1 = curr1.next

        while curr2:
            sum_value = curr2.val + carry
            value = sum_value % 10
            carry = sum_value // 10

            node = ListNode(value)
            curr.next = node
            curr = node
            curr2 = curr2.next

        if carry != 0:
            node = ListNode(1)
            curr.next = node
        
        return dummyNode.next