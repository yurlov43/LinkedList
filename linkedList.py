class Node:

    def __init__(self, v):
        self.value = v
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        matches_list = []
        node = self.head
        while node is not None:
            if node.value == val:
                matches_list.append(node)
            node = node.next
        return matches_list

    def delete(self, val, all=False):
        node_previous = self.head
        node_current = self.head
        while node_current is not None:
            if node_current.value == val:
                if node_current is self.head and node_current is self.tail:
                    self.head = None
                    self.tail = None
                elif node_current is self.head:
                    self.head = node_current.next
                    node_previous = self.head
                elif node_current is self.tail:
                    self.tail = node_previous
                    node_current = self.tail
                else:
                    node_previous.next = node_current.next
                if all is False:
                    return
            node_previous = node_current
            node_current = node_current.next

    def clean(self):
        self.head = None
        self.tail = None

    def len(self):
        node = self.head
        length = 0
        while node is not None:
            length += 1
            node = node.next
        return length

    def insert(self, after_node, new_node):
        if after_node is None and self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            node = self.head
            while node is not None:
                if node is after_node:
                    new_node.next = node.next
                    node.next = new_node
                    if node is self.tail:
                        self.tail = new_node
                node = node.next
