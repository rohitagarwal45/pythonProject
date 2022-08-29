# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self):
        self.head = ListNode()

    def push(self, lista):
        curr = self.head

        for ele in lista:
            new_node = ListNode(ele)
            curr.next = new_node
            curr = curr.next

    def display(self):
        curr = self.head.next

        while curr:
            print(curr.val)
            curr = curr.next

    def removeNthFromEnd(self, n):

        main_p = ref_p = prev = self.head.next
        count = 1
        while ref_p and count <= n:
            count += 1
            ref_p = ref_p.next

        while ref_p:
            prev = main_p
            main_p = main_p.next
            ref_p = ref_p.next

        if prev:
            prev.next = main_p.next

    def reverse(self):

        curr = self.head.next
        prev = next1 = None

        while curr:
            next1 = curr.next
            curr.next = prev
            prev = curr
            curr = next1

        self.head.next = prev
        a = 1

lista = [1, 2, 3, 4, 5]
index = 2

obj1 = Solution()
obj1.push(lista)
obj1.display()
# obj1.removeNthFromEnd(index)
# print("after deleting\n")
# obj1.display()
obj1.reverse()
print("after reverse : \n")
obj1.display()
