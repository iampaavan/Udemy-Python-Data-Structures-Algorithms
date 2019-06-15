import sys

n = 50

data = []

for i in range(n):

    # number of elements
    a = len(data)

    # Actual size in Bytes
    b = sys.getsizeof(data)

    print(f"Length: {a}; Size in Bytes: {b}")

    # increase Length by one
    data.append(i)