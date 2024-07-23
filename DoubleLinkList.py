class Node:
    def __init__(self, pre_node, data, next_node):
        self.pre = pre_node
        self.data = data
        self.next = next_node


class DoubleLinkList:
    def __init__(self):
        self.head = None

    def append_node(self, data):
        current_node = self.head
        if current_node:
            while current_node:
                if current_node.next:
                    current_node = current_node.next
                else:
                    new_node = Node(current_node, data, None)
                    current_node.next = new_node
                    break
        else:
            self.head = Node(None, data, None)

    def print_list(self):
        current_node = self.head
        while current_node:
            print("Data", current_node.data)
            current_node = current_node.next

    def append_any(self, append_point, data):
        current_node = self.head
        if current_node:
            while current_node:
                if current_node.data == append_point:
                    current_node.next = Node(current_node, data, current_node.next)
                    break
                current_node = current_node.next
        else:
            print("List is empty")


doubleLinkedList = DoubleLinkList()
doubleLinkedList.append_node(1)
doubleLinkedList.append_node(2)
doubleLinkedList.append_node(3)
doubleLinkedList.append_any(3, 3.1)
doubleLinkedList.append_node(4)
doubleLinkedList.append_node(5)
doubleLinkedList.print_list()
