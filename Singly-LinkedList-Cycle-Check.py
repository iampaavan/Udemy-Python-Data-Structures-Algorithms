from nose.tools import assert_equal


class SLLNode:

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"SLL Node Object: data={self.data}"


def cycle_check(node):

    marker1 = node
    marker2 = node

    while marker2 is not None and marker2.next is not None:

        marker1 = marker1.next
        marker2 = marker2.next.next

        if marker2 == marker1:
            return True

    return False


a = SLLNode(1)
b = SLLNode(2)
c = SLLNode(3)

a.next = b
b.next = c
c.next = a


x = SLLNode(1)
y = SLLNode(2)
z = SLLNode(3)

x.next = y
y.next = z

print(cycle_check(c))
print(cycle_check(x))


print(f'*******************************************************')


class TestCycleCheck(object):

    def test(self, sol):
        assert_equal(sol(a), True)
        assert_equal(sol(x), False)
        print(f"All Test Cases passed.")


t = TestCycleCheck()
t.test(cycle_check)