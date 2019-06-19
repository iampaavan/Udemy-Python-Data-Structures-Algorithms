class DLLNode:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

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
        pass

    def remove(self, data):
        pass