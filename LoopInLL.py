class Node:
    def __init__(self, val=None, next=None):
        self.data = val
        self.next = next


class LinkList:
    def __init__(self):
        self.head = Node()

    def push(self, element):
        curr = self.head
        new_node = Node(element)
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def check_loop(self):
        slow = fast = self.head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast.next == slow.next:
                return "link list contains string"

        return "Link list is linear"


llist = LinkList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(10)
llist.push(33)

# Create a loop for testing
print(llist.head.next.next.next.next.next.data)
print(llist.head.data)
llist.head.next.next.next.next.next = llist.head.next.next.next

print(f"{llist.check_loop()}")
