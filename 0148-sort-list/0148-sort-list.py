# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head):
        slow = head
        fast = head
        previous = None

        while fast and fast.next:
            previous = slow
            slow = slow.next
            fast = fast.next.next
        
        return previous
    
    def merge(self, node1, node2):
        dummyNode = ListNode()
        curr = dummyNode

        curr1 = node1
        curr2 = node2

        while curr1 and curr2:
            if curr1.val <= curr2.val:
                next = curr1.next
                curr.next = curr1
                curr = curr1
                curr.next = None
                curr1 = next
            else:
                next = curr2.next
                curr.next = curr2
                curr = curr2
                curr.next = None
                curr2 = next

        while curr1:
            next = curr1.next
            curr.next = curr1
            curr = curr1
            curr.next = None
            curr1 = next

        while curr2:
            next = curr2.next
            curr.next = curr2
            curr = curr2
            curr.next = None
            curr2 = next

        return dummyNode.next

    def mergeSort(self, node):
        if node is None or node.next is None:
            return node
        
        middle = self.middleNode(node)
        next_node = middle.next
        middle.next = None

        node1 = self.mergeSort(node)
        node2 = self.mergeSort(next_node)

        return self.merge(node1,node2)

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        return self.mergeSort(head)