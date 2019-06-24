def seq_search_unordered(array, element):

    position = 0
    found = False

    while position < len(array) and not found:

        if array[position] == element:
            found = True

        else:
            position += 1

    return found


print(seq_search_unordered([3, 2, 1, 5, 4], 6))
print(seq_search_unordered([3, 2, 1, 5, 4], 3))
print(seq_search_unordered([3, 2, 1, 5, 4], 4))
print(seq_search_unordered([3, 2, 1, 5, 4], 1))
