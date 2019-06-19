class SLLNode:

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f'SLL Node Object: data={self.data}'

    def get_data(self):
        return self.data

    def set_data(self, new_data):
        self.data = new_data

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next


class SLL:

    def __init__(self):
        self.head = None

    def __repr__(self):
        return f"SLL Node Object: head={self.head}"

    def is_empty(self):
        """Returns True if the Linked List is empty. Else returns False."""
        return self.head is None # self.head == None

    def add_front(self, new_data):
        """Add a Node whose data is the new_data argument to the front of the Linked List."""
        temp = SLLNode(new_data)
        temp.set_next(self.head)
        self.head = temp

    def size(self):
        """Traverses the Linked List and returns an integer value representing the number of nodes in
        the Linked list."""

        """The time complexity is O(n) because every Node in the Linked List must be visited in order
        to calculate the size of the Linked List."""
        size = 0
        if self.head is None:
            return 0

        current = self.head
        while current is not None: # While there are still Nodes left to count.
            size += 1
            current = current.get_next()

        return size

    def search(self, data):
        """Traverses the Linked List and returns True if the data searched for is present
        in one of the Nodes. Otherwise, it returns False."""

        """The time complexity is O(n) because in the worst case we need to traverse across all the nodes."""
        if self.head is None:
            return 'Linked List empty. No Nodes to search.'

        current = self.head
        while current is not None:
            # The Node's data matches what we're looking for
            if current.get_data() == data:
                return True

            # The Node's data doesn't match
            else:
                current = current.get_next()

        return False

    def remove(self, data):
        """Removes the first occurence of a Node that contains the data argument as its self.data variable.
        Returns nothing."""

        """The time complexity is O(n) because in the worst case we have to visit every Node before we find
        the one we need to remove."""
        if self.head is None:
            return 'Linked List empty. No nodes to remove.'

        current = self.head
        previous = None
        found = False

        while not found:
            if current.get_data() == data:
                found = True
                print(current.get_data())
            else:
                if current.get_next() is None:
                    return 'A Node with that data value is not present.'
                else:
                    previous = current
                    current = current.get_next()

        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())


sll = SLL()
print(sll.remove(1))

sll.add_front(1)
sll.add_front(2)
sll.add_front(3)

print(sll.remove(1))