#add operation ===> at beginning, at end
#==> at given pos(before given node, after node)


class Node:
    def __init__(self, data= None, next = None):
        self.data = data
        self.next = next

class Linked_List:
    def _init__(self):
        self.head = None
    
    def traverse(self):
        n = self.head
        while n:
            print(n.data, "->", end='')
            n = n.next
    
    def addstart(self, data):  #===> at beginning
        self.head = Node(data=data, next= self.head)
    
    def addend(self, data):  #===> at end
        new_node = Node(data= data)
        if (self.head == None):
            self.head = new_node
        else:
            n = self.head
            while n.next:
                n = n.next
            n.next = new_node

    def add_after(self, data, x):  #====> after given node
        n = self.head
        while n is not None:
            if x == n.data:
                break
            n = n.next
        if n is None:
            print("node is not present in ll")
        else:
            new_node = Node(data)
            new_node.next = n.next
            n.next = new_node

    def add_before(self, data, x):  # ===> before given node
        if self.head is None:
            print("Linked list is empty")
            return
        if self.head.data == x:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            return
        n = self.head
        while n.next

















