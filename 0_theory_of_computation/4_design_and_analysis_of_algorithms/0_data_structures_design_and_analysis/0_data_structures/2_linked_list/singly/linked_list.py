from singly.node import Node


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_top(self, data):
        node = Node(data)
        if self.head:
            node.next = self.head
            self.head = node
        else:
            self.head = node

    def remove_from_top(self):
        if self.head:
            node = self.head
            self.head = self.head.next
            return node.data
        else:
            raise ValueError("List is empty")

    def insert_at_end(self, data):
        node = Node(data)
        if self.head:
            current_node = self.head
            while (current_node.next):
                current_node = current_node.next
            current_node.next = node
        else:
            self.head = node

    def insert_after_value(self, predicate_value, data):
        if self.head == None:
            raise IndexError("The list is empty")

        current_node = self.head
        while (current_node):
            if current_node.data == predicate_value:
                current_node.next = Node(data, current_node.next)
                return
            current_node = current_node.next
