class TreeNode:
    def __init__(self,data):
        self.left=None
        self.data=data
        self.right=None



def BSFTraversing(treeNode):
    if treeNode:
        queue=[]
        queue.append(treeNode)

        while len(queue)>0:
            getNode=queue.pop(0)
            print(getNode.data)
            if getNode.left:
                queue.append(getNode.left)
            if getNode.right:
                queue.append(getNode.right)





tree= TreeNode(1)

# left side
tree.left=TreeNode(2)
tree.left.left=TreeNode(4)
tree.left.right=TreeNode(5)
# right side
tree.right=TreeNode(3)
tree.right.right=TreeNode(6)

BSFTraversing(tree)