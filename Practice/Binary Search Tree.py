class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        new_node=Node(new_val)
        if self.root==None:
            self.root=new_node
            return
        current=self.root
        while True:
            if current.value>new_val:
                if(current.left==None):
                    current.left=new_node
                    return
                else:
                    current=current.left
            else:
                if(current.right==None):
                    current.right=new_node
                    return
                else:
                    current=current.right
            

    def search(self, find_val):
        current=self.root
        while True:
            if current==None:
                return False
            elif current.value==find_val:
                return True
            elif current.value>find_val:
                current=current.left
            else:
                current=current.right
    
# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print(tree.search(4))
# Should be False
print(tree.search(6))