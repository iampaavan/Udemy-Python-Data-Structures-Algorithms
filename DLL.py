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
        pass

    def search(self, data):
        pass

    def add_front(self, new_data):
        pass

    def remove(self, data):
        pass