class Node:
    def __init__(self,data= None,next=None):
        self.data = data
        self.next = next
class Linked_List:
    def __init__(self):
        self.head = None
    def traverse(self):  # 321
        temp = self.head
        while temp:
            print(temp.data,'->', end='')
            temp = temp.next
    def addstart(self,data):
        self.head = Node(data=data,next=self.head)
    def addend(self,data):
        New_Node = Node(data=data)
        if(self.head == None):
            self.head = New_Node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = New_Node

ob1 = Linked_List()
ob1.addstart(1)
ob1.addstart(2)
ob1.addstart(3)
ob1.addstart(4)
ob1.traverse()
ob1.addend(5)
ob1.addend(6)
ob1.addend(7)
ob1.traverse()