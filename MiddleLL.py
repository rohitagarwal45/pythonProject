# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, lista):

        head = ListNode()
        curr = head
        for i in lista:
            newnode = ListNode(i)
            curr.next = newnode
            curr = curr.next

        p1 = head.next
        p2 = head.next
        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next

        print(p1.val)


lista = [1, 2, 3, 4, 5, 6, 7]
obj1 = Solution()
obj1.middleNode(lista)
