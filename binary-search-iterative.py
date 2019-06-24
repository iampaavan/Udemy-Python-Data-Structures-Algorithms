def binary_search(array, element):

    first = 0
    last = len(array) - 1
    found = False

    while first <= last and not found:

        mid = (first+last) // 2

        if array[mid] == element:
            found = True

        else:

            if element < array[mid]:
                last = mid - 1

            else:
                first = mid + 1

    return found


print(binary_search([1, 2, 3, 4, 5, 6, 7], 5))


