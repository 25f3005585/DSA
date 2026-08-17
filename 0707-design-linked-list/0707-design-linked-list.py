class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        
        curr = self.head
        i = 0

        while i < index:
            curr = curr.next
            i+=1
        
        return curr.val

    def addAtHead(self, val: int) -> None:
        if self.size == 0:
            node = Node(val)
            self.head = node
            self.tail = node
        else:
            node = Node(val)
            node.next = self.head
            self.head.prev = node
            self.head = node
        
        self.size += 1
        return

    def addAtTail(self, val: int) -> None:
        if self.size == 0:
            node = Node(val)
            self.head = node
            self.tail = node
        else:
            node = Node(val)
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        
        self.size += 1
        return

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        
        if index == 0:
            return self.addAtHead(val)

        if index == self.size:
            return self.addAtTail(val)

        curr = self.head
        i = 0

        while i < index:
            curr = curr.next
            i+=1

        node = Node(val)
        node.next = curr
        previous = curr.prev
        curr.prev = node
        node.prev = previous
        previous.next = node
        self.size += 1
        return

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        
        if index == 0:
            if self.size == 1:
                self.head = None
                self.tail = None
            else:
                node = self.head.next
                self.head = node
                self.head.prev = None
            self.size -= 1
            return
        
        if index == self.size - 1:
            if self.size == 1:
                self.head = None
                self.tail = None
            else:
                prev = self.tail.prev
                self.tail = prev
                self.tail.next = None
            self.size -= 1
            return
        
        curr = self.head
        i = 0

        while i < index:
            curr = curr.next
            i+=1
        
        curr.prev.next = curr.next
        curr.next.prev = curr.prev

        curr.next = None
        curr.prev = None
        self.size -= 1
        return


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)