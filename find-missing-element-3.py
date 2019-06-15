def missing(array1, array2):

    result = 0

    for number in array1 + array2:

        result ^= number

    return result


print(missing([1, 2, 3, 4, 5, 6, 7], [3, 7, 2, 1, 4, 6]))
