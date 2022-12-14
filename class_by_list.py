class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return f'LinkedList contains {self.value}'

    def update(self, value):
        """Updates value of the Node object"""
        self.value = value
        return self.value

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

    def __len__(self):
        '''Returns number of Nodes in the list.
        When this method defined, built-in len function can be called on class instances
        '''
        lenght = 0
        current_node = self.head
        while current_node is not None:
            lenght += 1
            current_node = current_node.next
        return lenght


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

    def is_empty(self):
        """Returns True if there no Nodes in the list, False otherwise"""
        if self.length == 0:
            return True
        else:
            return False

    def pop(self):
        '''Removes last Node from the list and returns it'''
        pass

    def copy(self):
        '''Returns a copy of linked list. Any changes of copy would not affect
        original list
        '''
        newLinkedList = LinkedList()
        current = self.head
        while current is not None:
            newNode = Node(current.value)
            newLinkedList.add_to_tail(newNode)
            current = current.next
        return newLinkedList

    def sorted(self):
        '''Returns a copy of linked list, sorted in ascending order -
        Node with smallest value goes first. Original list will not be
        changed by this method
        '''
        pass

    def reversed(self):
        '''Returns a copy of the linked list where Nodes are oredered in reverse order:
        head node of original list becomes a tail for copy
        '''
        pass
    def is_palindrome(self):
        '''A palindrome is a sequence that reads the same forward and backward.
        Method returns True if current list is a palindorome, False otherwise
        '''
        pass


if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.add_to_tail(1)
    linked_list.add_to_tail(2)
    linked_list.add_to_head(5)
    linked_list.add_to_head(10)

    for node in linked_list:
        print(node)
    assert len(linked_list) == 4
    assert linked_list.is_empty() == False
    # assert linked_list.pop().value == 2
    # list_copy = linked_list.copy()
    # list_copy.add_to_tail(12)
    # assert len(list_copy) != len(linked_list)
    # sorted_copy = linked_list.sorted()
    # assert linked_list.is_palindrome() == False
    # assert linked_list.reversed().head.value == 1