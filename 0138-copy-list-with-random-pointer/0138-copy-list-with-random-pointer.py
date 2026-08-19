"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return head
        curr = head

        while curr:
            next = curr.next
            node = Node(curr.val)
            node.next = curr.next
            curr.next = node
            curr = next

        
        curr = head
        while curr and curr.next:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
        
        dummyNode = Node(0)
        node = dummyNode

        curr = head.next

        while curr and curr.next:
            next = curr.next.next
            node.next = curr
            node = curr
            curr = next

        if curr:
            node.next = curr
        else:
            node.next = None

        return dummyNode.next
