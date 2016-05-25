class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def get_data(self):
        return self.data

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def set_left(self, left):
        self.left = left

    def set_right(self, right):
        self.right = right
def sum_tree(node):
    if not(node.get_left() or node.get_right()):
        #print('has no children')
        return node.get_data()
    elif node.get_left() and node.get_right():
        #print('has two children')
        return node.get_data() + sum_tree(node.get_left()) + sum_tree(node.get_right())
    elif not node.get_left():
        #print('has right child')
        return node.get_data() + sum_tree(node.get_right())
    elif not node.get_right():
        #print('has left child')
        return node.get_data() + sum_tree(node.get_left())

root = Node(1)
print('expecting 1:', end='\t')
print(sum_tree(root))

root.set_left(Node(2))
print('expecting 3:', end='\t')
print(sum_tree(root))

root.set_right(Node(3))
print('expecting 6:', end='\t')
print(sum_tree(root))

root.get_left().set_left(Node(4))
print('expecting 10:', end='\t')
print(sum_tree(root))

root.get_right().set_left(Node(5))
print('expecting 15:', end='\t')
print(sum_tree(root))

root.get_right().set_right(Node(6))
print('expecting 21:', end='\t')
print(sum_tree(root))

root.get_right().get_right().set_left(Node(7))
print('expecting 28:', end='\t')
print(sum_tree(root))
