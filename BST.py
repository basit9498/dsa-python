class TreeNode:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None


# data = [22, 33, 17, 14, 23, 8, 5, 21, 26, 15, 13]
data=[50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45, 55, 65, 75, 85, 5, 15, 28, 53, 58, 82, 90, 12, 83]



def makeBST(arrData):
    rootNode = None
    if (len(arrData)):
        rootNode = TreeNode(arrData[0])

    for x in range(1, len(arrData)):
        tempNode = rootNode
        while tempNode:
            #  right side
            if arrData[x] >= tempNode.data:
                if not tempNode.right:
                    tempNode.right = TreeNode(arrData[x])
                    tempNode = None
                else:
                    tempNode = tempNode.right

            else:
                #    come to left side
                if not tempNode.left:
                    tempNode.left = TreeNode(arrData[x])
                    tempNode = None
                else:
                    tempNode = tempNode.left

    return rootNode


rootNode = makeBST(data)


def preOrder(node):
    if node:
        preOrder(node.left)
        print(node.data)
        preOrder(node.right)

def deletebstnode(root,data):
    parent=None
    temp=root
    treeHeight=0
    while temp:
        if temp.data == data:
            # this condition for if we have no leaf left and right
            if not temp.left and not temp.right:
                if parent.left and parent.left.data == data:
                    parent.left=None
                elif parent.right and parent.right.data == data:
                    parent.right=None
            # if right or left have only one child so we just replaced them
            elif temp.left and not temp.right:
                parent.right=temp.left
            elif not temp.left and temp.right:
                parent.left=temp.right
            # if
            elif temp.left and temp.right:
                #     using in-order successor

                findSmallestValueNode=temp.right
                currentValue=findSmallestValueNode.data
                successorParent=temp.right
                # if left have the child node
                if findSmallestValueNode.left:
                    while findSmallestValueNode:
                        print("left node value:",findSmallestValueNode.data)
                        successorParent=findSmallestValueNode
                        findSmallestValueNode=findSmallestValueNode.left
                        if not findSmallestValueNode.left:
                            parent=temp
                            parent.data=findSmallestValueNode.data
                            if findSmallestValueNode.right:
                                successorParent.left=findSmallestValueNode.right
                            findSmallestValueNode=None


                else:
                    # Replace the value with the deleted data
                    parent=temp
                    parent.data=currentValue
                    parent.right=None


            break
        parent=temp
        if data > temp.data:
            temp=temp.right
        else:
            temp=temp.left
        treeHeight= treeHeight+1

    return root

print("Before the Delete Tree")
preOrder(rootNode)

deletePoint=10
rootNode=deletebstnode(rootNode,deletePoint)

print("After the Delete Tree: ",deletePoint)
preOrder(rootNode)
