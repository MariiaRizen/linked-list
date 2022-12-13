class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return f'LinkedList contains {self.value}'


class LinkedList:

    def __init__(self):
        self.head = None

    def __iter__(self):
        return self

    def __next__(self):
        if self.head is None:
            raise StopIteration
        else:
            head, self.head = self.head, self.head.next
        return head

    def add_to_tail(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node

    def add_to_head(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node


if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.add_to_tail(1)
    linked_list.add_to_tail(2)
    linked_list.add_to_head(5)
    linked_list.add_to_head(10)

    for node in linked_list:
        print(node)