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
