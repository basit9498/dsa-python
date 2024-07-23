class Node:
    def __init__(self, data):
        self.next = None
        self.data = data


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        current_top = self.top
        if current_top:
            new_node = Node(data)
            new_node.next = current_top
            self.top = new_node

        else:
            self.top = Node(data)

    def pop(self):
        if self.top:
            print("Pop:", self.top.data)
            self.top = self.top.next

        else:
            print("No Data found")

    def print_list(self):
        current_top = self.top
        while current_top:
            print("Data", current_top.data)
            current_top = current_top.next


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.print_list()
stack.pop()
print("after pop the data")
stack.print_list()
stack.pop()
print("after pop the data")
stack.push(10)
stack.push(33)
stack.print_list()
