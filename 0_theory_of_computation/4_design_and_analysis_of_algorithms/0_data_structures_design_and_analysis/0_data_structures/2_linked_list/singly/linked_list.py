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

    def insert_values(self, values: list):
        """
            Insert iterable of values to the end
        """
        # O(N). N = length of current values in list

        def _insert_values(start_index):
            # O(M). M = length of new values
            current_node = self.head
            while (current_node.next):
                current_node = current_node.next

            idx = start_index
            while (idx < len(values)):
                current_node.next = Node(values[idx])
                current_node = current_node.next
                idx += 1

        if self.head == None:
            self.head = Node(values[0])
            _insert_values(1)
        else:
            _insert_values(0)

        # Total = O(N + M) = O(N) | O(M) depending on which is longer. Therefore Linear = O(N)

        # alternative
        # for v in values:
        #     self.insert(v)
        # O(N * M)
            # N = length of current values in list
            # M = length of new values
            # if M = N, then O(N*N) = O(N^2)

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
