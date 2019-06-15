def missing(array1, array2):

    array1.sort()
    array2.sort()

    for num1, num2 in zip(array1, array2):
        if num1 != num2:
            return num1

    return array1[-1]


print(missing([1, 2, 3, 4, 5, 6, 7], [3, 7, 2, 1, 4, 6]))
print(missing([20, 21, 22, 23, 24, 25, 26, 27], [20, 22, 23, 24, 25, 26, 27]))