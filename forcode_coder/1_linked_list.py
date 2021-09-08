class Node:
    def __init__(self, data= None, next= None):
        self.data = data
        self.next = next
class Linked_list:
    def __init__(self):
        self.head = None
        
ob1 = Linked_list()
ob1.head = Node(15)

second = Node(3)
third = Node(17)
fourth = Node(90)

ob1.head.next = second
second.next = third
third.next = fourth
print(ob1.head.data)
print(ob1.head.next.data)
print(ob1.head.next.next.data)
print(ob1.head.next.next.next.data)
        