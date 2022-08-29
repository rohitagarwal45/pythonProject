class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

        # print(value)


class Link_list:
    def __init__(self):
        self.head = Node()
        # self.count = 0

    def append(self, data):
        # self.count +=1
        new_node = Node(data)
        curr = self.head
        while curr.next != None:
            curr = curr.next
        curr.next = new_node

    def display(self):
        curr = self.head.next
        while curr.next != None:
            print(curr.value)
            print(f"current address is {curr.next} ")
            curr = curr.next
        print(curr.value)

    def GetNthNode(self,n):
        curr = self.head.next
        count = 0
        while curr.next != None:
            count += 1
            curr = curr.next
            if count == n:
                return curr.value

lista = list(map(int,input("Enter the list : ").split()))
n = int(input("Enter Nth number : "))
llist = Link_list()

for i in lista:
    llist.append(i)

value = llist.GetNthNode(n)
if value:
    print(value)
else:
    print("Not found")
# llist.display()







