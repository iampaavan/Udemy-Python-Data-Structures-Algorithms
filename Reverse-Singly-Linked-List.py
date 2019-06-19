class SLLNode(object):

    def __init__(self, data):
        self.data = data
        self.next_node = None

    def __repr__(self):
        return 'SLL Node Object: data={}'.format(self.data)


def reverse(head):
    current = head
    previous = None

    while current:
        next_node = current.next_node
        current.next_node = previous

        previous = current
        current = next_node

    return previous


a = SLLNode(1)
b = SLLNode(2)
c = SLLNode(3)
d = SLLNode(4)

a.next_node = b
b.next_node = c
c.next_node = d

print(a.next_node.data)
print(b.next_node.data)
print(c.next_node.data)

reverse(a)

print(d.next_node.data)
print(c.next_node.data)
print(b.next_node.data)