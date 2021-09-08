# add operation====> at beginning, at end,
# ==> at given pos(before given node, after node)

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class Linked_List:
    def __init__(self):
        self.head = None

    def traverse(self):  # 321
        temp = self.head
        while temp:
            print(temp.data, '->', end='')
            temp = temp.next

    def addstart(self, data):  # ===> at beginning
        self.head = Node(data=data, next=self.head)

    def addend(self, data):  # ===> at end
        New_Node = Node(data=data)
        if(self.head == None):
            self.head = New_Node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = New_Node

    def add_after(self,data,x):  # ===> after given node
        n = self.head
        while n is not None:
            if x==n.data:
                break
            n = n.next
        if n is None:
            print("node is not presesnt in LL")
        else:
            new_node = Node(data)
            new_node.next = n.next
            n.next = new_node

    def add_before(self, data, x):  # ===> before given node
        if self.head is None:
            print("Linked List is empty!")
            return
        if self.head.data == x:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            return
        n = self.head
        while n.next is not None:
            if n.next.data == x:
                break
            n = n.next
        if n.next is None:
            print("Node is not found!")
        else: 
            new_node = Node(data)
            new_node.next = n.next
            n.next = new_node

ob1 = Linked_List()
ob1.addstart(1)
ob1.addstart(2)
ob1.addend(5)
ob1.addend(6)

ob1.add_after(10, 6)

ob1.add_before(7, 6)
ob1.traverse()



