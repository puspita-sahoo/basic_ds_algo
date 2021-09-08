#linked list start code 
#start of linked lst creation

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

l = Linked_list()
l.print_ll()

