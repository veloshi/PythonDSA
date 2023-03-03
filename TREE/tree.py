class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
    
    def insert(self,data):
        if self.val:
            if data < self.val :
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.val:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.val = data

    def printTree(self):
        if self.left is not None:
            self.left.printTree()
        print(self.val)
        if self.right is not None:
            self.right.printTree()

root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
root.printTree()