def binary_search(array, element):

    # Base Case
    if len(array) == 0:
        return False

    else:

        mid = len(array) // 2

        if array[mid] == element:
            return True

        else:

            if element < array[mid]:
                return binary_search(array[:mid], element)

            else:
                return binary_search(array[mid+1:], element)


print(binary_search([1, 2, 3, 4, 5, 6, 7], 5))