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
        pass

    def search(self, data):
        pass

    def remove(self, data):
        pass


sll = SLL()
print(sll.is_empty())

sll.add_front('berry')
print(sll.head)
print(sll.is_empty())