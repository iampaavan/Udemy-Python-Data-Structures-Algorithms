class Deque(object):

    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.items == []

    def addFront(self, data):
        self.items.insert(0, data)

    def addRear(self, data):
        self.items.append(data)

    def removeFront(self):
        if self.items:
            return self.items.pop(0)
        return 'Deque empty. No items to remove from the front.'

    def removeRear(self):
        if self.items:
            return self.items.pop()
        return 'Deque empty. No items to remove from the rear.'

    def peekFront(self):
        if self.items:
            return self.items[0]
        return 'Deque empty. No items at the front.'

    def peekRear(self):
        if self.items:
            return self.items[-1]
        return 'Deque empty. No itmes at the rear.'


d = Deque()
print(d.size())
print(d.is_empty())

print(d.peekFront())
print(d.peekRear())
print(d.removeFront())
print(d.removeRear())

d.addFront('hello')
d.addRear('world')
print(d.peekFront() + ' ' + d.peekRear())