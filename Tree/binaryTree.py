class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data< self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            
            if data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()

    # Left->Root->Right
    def InOrderTravers(self,root):
        inOrderArray = []
        if root:
            inOrderArray = self.InOrderTravers(root.left)
            inOrderArray.append(root.data)
            inOrderArray = inOrderArray + self.InOrderTravers(root.right)
        return inOrderArray
    # Root -> Left -> Right
    def preOrder(self,root):
        preOrderArray = []
        if root:
            preOrderArray.append(root.data)
            preOrderArray= preOrderArray + self.preOrder(root.left)
            preOrderArray= preOrderArray + self.preOrder(root.right)
        return preOrderArray

root = Node(10)
root.insert(6)
root.insert(12)
root.insert(5)
root.insert(7)
root.insert(4)
root.insert(16)
root.insert(13)
root.printTree()
print(root.InOrderTravers(root))
print(root.preOrder(root))
