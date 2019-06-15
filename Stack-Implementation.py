class Stack(object):

    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        if len(self.items) == 0:
            return 'Stack empty. No elements to remove.'
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def peek(self):
        if len(self.items) == 0:
            return 'Stack empty. No element at top of Stack.'
        return self.items[len(self.items) - 1]


s = Stack()
print(s.is_empty())

print(s.peek())
print(s.pop())

s.push(1)
s.push('two')

print(s.is_empty())
print(s.peek())

s.push(True)
print(s.size())