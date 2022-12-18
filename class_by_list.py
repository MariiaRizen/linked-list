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
        self.current = None
        self.end_iteration = False

    def __iter__(self):
        return self

    def __next__(self):
        current = self.current or self.head
        if self.end_iteration is True:
            self.end_iteration = False
            raise StopIteration
        else:
            node = current
            self.current = current.next
            if self.current is None:
                self.end_iteration = True

        return node



    def __len__(self):
        '''Returns number of Nodes in the list.
        When this method defined, built-in len function can be called on class instances
        '''
        length = 0
        current_node = self.head
        while current_node is not None:
            length = length + 1
            current_node = current_node.next
        return length


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
        if self.head is None:
            return True
        else:
            return False

    def pop(self):
        """Removes last Node from the list and returns it"""
        if self.head is None:
            return None
        elif self.head.next == None:
            pop_node = self.head
            self.head = None
            return pop_node
        else:
            secondlast = self.head
            while secondlast.next.next is not None:
                secondlast = secondlast.next
            pop_node = secondlast.next
            secondlast.next = None
            return pop_node



    def copy(self):
        '''Returns a copy of linked list. Any changes of copy would not affect
        original list
        '''
        newLinkedList = LinkedList()
        current = self.head
        while current is not None:
            newNode = Node(current.value)
            newLinkedList.add_to_tail(newNode.value)
            current = current.next
        return newLinkedList

    def sorted(self):
        '''Returns a copy of linked list, sorted in ascending order -
        Node with smallest value goes first. Original list will not be
        changed by this method
        '''
        sorted_linked_list = LinkedList()
        l = []
        for element in self:
            l.append(element.value)
        for element in sorted(l):
            sorted_linked_list.add_to_tail(element)
        return sorted_linked_list

    def reversed(self):
        """Returns a copy of the linked list where Nodes are oredered in reverse order:
        head node of original list becomes a tail for copy
        """

        reversed_linked_list = LinkedList()
        l = []
        for element in self:
            l.append(element.value)
        for element in reversed(l):
            reversed_linked_list.add_to_tail(element)
        return reversed_linked_list

    def is_palindrome(self):
        '''A palindrome is a sequence that reads the same forward and backward.
        Method returns True if current list is a palindorome, False otherwise
        '''
        l = []
        for element in self:
            l.append(element.value)
        reversed_list = l[::-1]
        if l == reversed_list:
            return True
        else:
            return False




if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.add_to_tail(1)
    linked_list.add_to_tail(2)
    linked_list.add_to_head(5)
    linked_list.add_to_head(10)

    # for node in linked_list:
    #     print(node)
    assert len(linked_list) == 4
    assert linked_list.is_empty() == False
    assert linked_list.pop().value == 2
    list_copy = linked_list.copy()
    list_copy.add_to_tail(12)
    assert len(list_copy) != len(linked_list)
    sorted_copy = linked_list.sorted()
    assert linked_list.is_palindrome() == False
    assert linked_list.reversed().head.value == 1

