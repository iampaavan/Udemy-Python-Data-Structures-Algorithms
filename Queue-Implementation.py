class Queue(object):

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def enqueue(self, data):
        return self.items.insert(0, data)

    def dequeue(self):
        if len(self.items) == 0:
            return 'Queue empty. No items to remove.'
        return self.items.pop()

    def peek(self):
        if len(self.items) == 0:
            return 'Queue empty. No items to at the end of the queue.'
        return self.items[len(self.items) - 1]


q = Queue()
print(q.is_empty())
print(q.peek())
print(q.dequeue())
print(q.size())

q.enqueue(1)
q.enqueue('two')
print(q.is_empty())
print(q.peek())
print(q.dequeue())
print(q.size())