class Node:
    def __init__(self, data):
        self.next = None
        self.data = data


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.tail:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node

    def dequeue(self):
        if self.head:
            print("Dequeue:", self.head.data)
            temp_head = self.head
            self.head = temp_head.next
        else:
            print("List is empty")

    def print_list(self):
        current_head = self.head
        if current_head:
            while current_head:
                print("List Data:", current_head.data)
                current_head = current_head.next
        else:
            print("List is empty")


queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.print_list()
print("After Dequeue")
queue.dequeue()
queue.enqueue(5)
queue.print_list()
