from collections import defaultdict


def missing(array1, array2):

    d = defaultdict(int)

    for num in array2:
        d[num] += 1

    for num in array1:
        if d[num] == 0:
            return num

        else:
            d[num] -= 1


print(missing([1, 2, 3, 4, 5, 6, 7], [3, 1, 7, 2, 1, 4, 6]))
print(missing([20, 21, 22, 23, 24, 25, 26, 27], [20, 22, 23, 24, 25, 26, 27]))
