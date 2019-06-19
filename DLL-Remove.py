class DLLNode:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

    def __repr__(self):
        return f'DLL Node Object: data={self.data}'

    def get_data(self):
        return self.data

    def set_data(self, new_data):
        self.data = new_data

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next

    def get_previous(self):
        return self.previous

    def set_previous(self, new_previous):
        self.previous = new_previous


class DLL:

    def __init__(self):
        self.head = None

    def __repr__(self):
        return f'<DLL Object: head={self.head}>'

    def is_empty(self):
        return self.head is None

    def size(self):
        """Traverses the Linked List and returns an integer value representing the number of nodes in
        the Linked list."""

        """The time complexity is O(n) because every Node in the Linked List must be visited in order
        to calculate the size of the Linked List."""
        size = 0
        if self.head is None:
            return 0

        current = self.head
        while current is not None:
            current = current.get_next()
            size += 1

        return size

    def search(self, data):
        """Traverses the Linked List and returns True if the data searched for is present
        in one of the Nodes. Otherwise, it returns False."""

        """The time complexity is O(n) because in the worst case we need to traverse across all the nodes."""
        if self.head is None:
            return 'Linked List is empty. No data to search.'

        current = self.head
        while current is not None:
            if current.get_data() == data:
                return True
            else:
                current = current.get_next()
        return False

    def add_front(self, new_data):
        """Add a Node whose data is the new_data argument to the front of the Linked List."""
        temp = DLLNode(new_data)
        temp.set_next(self.head)

        if self.head is not None:
            self.head.set_previous(temp)

        self.head = temp

    def remove(self, data):
        """Removes the first occurrence of a Node that contains the data argument as its self.data attribute.
        Returns nothing."""

        """The time complexity is O(n) because in the worst case, we have to visit every Node before finding the
        one we want to remove."""
        if self.head is None:
            return 'Linked List is empty. No Nodes to remove.'

        current = self.head
        found = False
        while not found:
            if current.get_data() == data:
                found = True
            else:
                if current.get_next() is None:
                    return 'A node with that data value is not present.'
                else:
                    current = current.get_next()

        if current.previous is None:
            self.head = current.get_next()

        else:
            current.previous.set_next(current.get_next())
            current.next.set_previous(current.get_previous())


dll = DLL()
print(dll.remove('bird'))

dll.add_front(5)
dll.add_front('apple')

print(dll.remove(1))

dll.add_front('bird')
dll.remove('apple')

print(dll.head.next)
print(dll.head.previous)
