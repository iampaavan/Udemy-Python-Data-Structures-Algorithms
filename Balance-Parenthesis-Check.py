class Stack(object):

    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        if len(self.items) == 0:
            return 'Stack is empty. No items to remove.'
        return self.items.pop()

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.items == []

    def peek(self):
        if self.items:
            return self.items[-1]
        return 'Stack empty. No items at the top of the stack.'


def balance_check(string):

    # Edge Case:
    if len(string) % 2 != 0:
        return False

    s = Stack()

    opening = set('{[(')
    matches = set((('(', ')'), ('{', '}'), ('[', ']')))

    for parenthesis in string:

        if parenthesis in opening:
            s.push(parenthesis)

        else:

            if s.size() == 0:
                return False

            else:
                last_open = s.pop()

                if (last_open, parenthesis) not in matches:
                    return False

    return s.size() == 0


print(balance_check('[](){([[[]]])}'))
print(balance_check('()(){]}'))
