import math


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

    def find_middle(self):
        arr = []
        current_node = self.head
        while current_node:
            arr.append(current_node.data)
            current_node = current_node.next

        arr_len = len(arr)
        print(arr_len)
        if arr_len % 2 == 0:
            print("Even number in length")
            middle_index=int(arr_len/2)
            print("two middle:",arr[middle_index-1],arr[middle_index])
        else:
            print("Odd number in length")
            index=math.ceil(arr_len / 2)
            print("Middle:",index )
            print("Value is:",arr[index-1])


LinkList = SignleLinkList()
LinkList.append_node(Node(2))
LinkList.append_node(Node(4))
LinkList.append_node(Node(1))
LinkList.append_node(Node(5))
LinkList.append_node(Node(6))
LinkList.append_node(Node(9))
LinkList.append_node(Node(8))
LinkList.append_node(Node(7))
LinkList.append_node(Node(10))

LinkList.find_middle()
# LinkList.print_list()
