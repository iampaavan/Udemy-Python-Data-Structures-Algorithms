import ctypes, sys


class DynamicArray(object):

    def __init__(self):
        self.n = 0
        self.capacity = 1
        self.A = self.make_array(self.capacity)

    def __len__(self):

        return self.n

    def __getitem__(self, item):

        if not 0 <= item <= self.n:
            return IndexError("{} is out of bounds!".format(item))

        return self.A[item]

    def append(self, element):

        if self.n == self.capacity:
            self._resize(2 * self.capacity) # 2X if capacity isn't enough

        self.A[self.n] = element
        self.n += 1

    def _resize(self, new_capacity):

        B = self.make_array(new_capacity)

        for k in range(self.n):
            B[k] = self.A[k]

        self.A = B
        self.capacity = new_capacity

    def make_array(self, new_capacity):

        return (new_capacity * ctypes.py_object)()


array = DynamicArray()


array.append(1)
print(array.__len__())


array.append(2)
print(array.__len__())


array.append(3)
print(array.__len__())


array.append(4)
print(array.__len__())


print(array[0])
print(array[3])

for i in range(10):

    array.append(i)

    a = len(array)

    # Actual size in Bytes
    b = sys.getsizeof(array)
    print(f"Length: {a}; Size in Bytes: {b}")

