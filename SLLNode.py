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


node1 = SLLNode(1)
print(node1.get_data())
node2 = SLLNode(2)
node1.set_next(node2)
print(node1.get_next())