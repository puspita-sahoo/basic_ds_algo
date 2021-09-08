"""
#     Depth  First Traversal
]
1 = Inorder = (left root right)
2 = preorder = ( root left right)
3 = postorder = (left right  root)
# Breath First Traversal
1. Level ORder Traversal
     1  first.left.left.data
    / \
   2   3
 / \  / \
4  5 6   7
inorder = 4,2,5,1,6,3,7
preorder = 1,2,4,5,3,6,7
postorder = 4,5,2,6,7,3,1
levelorder = 1,2,3,4,5,6,7
"""


class node:
    def __init__(self,data=None):
        self.data = data
        self.left_node = None
        self.right_node = None
class BinaryTree:
    def __init__(self):
        self.root = None
    def inorder(self):
        if(self.root == None):
            print("Tree Is Empty....")
        else:
            self._inorder(self.root)
    def _inorder(self,current):
        if current:
            self._inorder(current.left_node)
            print(current.data,end=" ")
            self._inorder(current.right_node)

ob1 = BinaryTree()
first = node(1)
second = node(2)
third = node(3)
fourth = node(4)
fifth = node(5)
sixth = node(6)
seventh = node(7)
ob1.root = first
first.left_node = second
first.right_node = third
second.left_node = fourth
second.right_node = fifth
third.left_node = sixth
third.right_node = seventh
print('Inorder : ',end=" ")
ob1.inorder()
