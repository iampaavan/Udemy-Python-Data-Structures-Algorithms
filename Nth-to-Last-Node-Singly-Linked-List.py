class SLLNode(object):

    def __init__(self, data):
        self.data = data
        self.next_node = None

    def __repr__(self):
        return 'SLL Node Object: data={}'.format(self.data)


def nth_to_last_node(N, head):

    left_pointer = head
    right_pointer = head

    for i in range(N - 1):

        if not right_pointer.next_node:
            raise LookupError('{} value is greater than the Linked List.'.format(N))

        right_pointer = right_pointer.next_node

    while right_pointer.next_node:
        left_pointer = left_pointer.next_node
        right_pointer = right_pointer.next_node

    return left_pointer


a = SLLNode(1)
b = SLLNode(2)
c = SLLNode(3)
d = SLLNode(4)
e = SLLNode(5)

a.next_node = b
b.next_node = c
c.next_node = d
d.next_node = e

print(nth_to_last_node(2, a))
