class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SignleLinkList:
    def __init__(self):
        self.head = None

    def append_node(self, node):
        current_node = self.head
        if current_node:
            while current_node:
                print(current_node.next)
                if current_node.next:
                    current_node = current_node.next
                else:
                    current_node.next = node
                    break
        else:
            self.head = node

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next


LinkList = SignleLinkList()
LinkList.append_node(Node(1))
LinkList.print_list()
LinkList.append_node(Node(2))
LinkList.print_list()
