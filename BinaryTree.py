class TreeNode:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None


treeNode = TreeNode(2)
# left side of the main root
treeNode.left = TreeNode(4)
treeNode.left.left = TreeNode(5)
treeNode.left.right = TreeNode(7)
treeNode.left.right.left = TreeNode(6)

# right side of the main root
treeNode.right = TreeNode(9)
treeNode.right.left = TreeNode(1)
treeNode.right.right = TreeNode(3)


# Pre Order Traversing

def preOrderTraversing(node):
    if node:
        print("Node Value:", node.data)
        preOrderTraversing(node.left)
        preOrderTraversing(node.right)


def inOrderTraversing(node):
    if node:
        inOrderTraversing(node.left)
        print("Node Value ", node.data)
        inOrderTraversing(node.right)


def postOrderTraversing(node):
    if node:
        postOrderTraversing(node.left)
        postOrderTraversing(node.right)
        print("Node Value:", node.data)


print("preOrderTraversing:-----------------")
preOrderTraversing(treeNode)
print("inOrderTraversing:-----------------")
inOrderTraversing(treeNode)
print("postOrderTraversing:-----------------")
postOrderTraversing(treeNode)
