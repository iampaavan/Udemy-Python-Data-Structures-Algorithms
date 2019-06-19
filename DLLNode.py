class DLLNode:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

    def __repr__(self):
        return f"DLL Node Object: data={self.data}"

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next

    def get_data(self):
        return self.data

    def set_data(self, new_data):
        self.data = new_data

    def get_previous(self):
        return self.previous

    def set_previous(self, new_previous):
        self.previous = new_previous


d1 = DLLNode(1)
d2 = DLLNode(2)

d2.set_previous(d1)
print(d2.get_previous())
d1.set_next(d2)
print(d1.get_next())