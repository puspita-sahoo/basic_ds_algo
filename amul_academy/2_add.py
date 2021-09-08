#Adding elements at the beginning Of the linked list | Program


class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None
class Linked_list:
    def __init__(self):
        self.head = None
    def print_ll(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref

    def add_begin(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node        

    def add_before(self,data,x):
        if self.head is None:
            print("Linked List is empty!")
            return
        if self.head.data==x:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            return
        n = self.head
        while n.ref is not None:
            if n.ref.data==x:
                break
            n = n.ref        
        if n.ref is None:
            print("Node is not found!")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node     

ll1 = Linked_list()
# ll1.add_begin(10)
# ll1.add_before(20, 10)
ll1.print_ll()
