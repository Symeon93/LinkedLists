class Node:
    """
    This class creates a new node every time is being called.
    """

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    """
    Within this class we will implement methods to append, remove, insert
    new elements in a linked list.
    """

    def __init__(self):
        self.head = None

    def prepend(self, value):
        """ Prepend a value to the beginning of the list. """
        if self.head is None:
            self.head = Node(value)
            return
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def append(self, value):
        """ Append a value to the end of the list. """

        if self.head is None:
            self.head = Node(value)
            return
        node = self.head
        while node.next:
            node = node.next
        node.next = Node(value)

    def search(self, value):
        """ Search the linked list for a node with the requested value and return the node. """
        node = self.head
        while node:
            if node.value == value:
                return node
            node = node.next
        raise ValueError('Value not found')

    def remove(self, value):
        """ Remove first occurrence of value. """
        if self.head is None:
            return

        if self.head.value == value:
            self.head = self.head.next
            return

        node = self.head
        while node.next:
            if node.next.value == value:
                node.next = node.next.next
                return
            node = node.next

    def pop(self):
        """ Return the first node's value and remove it from the list. """
        if self.head is None:
            return
        output = self.head.value
        self.head = self.head.next
        return output

    def insert(self, value, pos):
        """ Insert value at pos position in the list. If pos is larger than the
        length of the list, append to the end of the list. """

        if self.head is None:
            self.head = Node(value)
            return

        if pos == 0:
            self.prepend(value)
            return

        index = 0
        node = self.head
        while node.next and index <= pos:
            if (pos - 1) == index:
                new_node = Node(value)
                new_node.next = node.next
                node.next = new_node
                return

            index += 1
            node = node.next
        else:
            self.append(value)

    def size(self):
        """ Return the size or length of the linked list. """
        if self.head is None:
            return None
        shape = 0
        node = self.head
        while node:
            shape += 1
            node = node.next
        return shape

    def reverse(linked_list):
        """
        Reverse the inputted linked list
        """

        new_list = LinkedList()
        for element in linked_list:
            new_list.prepend(element)
        return new_list

    def __to_list__(self):
        """
        Uses as an argument the head of the linked list
        traverses the entire (linked) list and
        returns its counterpart array.
        """
        out = []
        node = self.head
        while node:
            out.append(node.value)
            node = node.next
        return out
