def seq_search_ordered(array, element):

    position = 0
    found = False
    stopped = False

    while position < len(array) and not found and not stopped:

        if array[position] == element:
            found = True

        else:

            if array[position] > element:
                stopped = True

            else:
                position += 1

    return found


print(seq_search_ordered([1, 2, 3, 4, 5, 6, 7], 1))
print(seq_search_ordered([1, 2, 3, 4, 5, 6, 7], 7))
print(seq_search_ordered([1, 2, 3, 4, 5, 6, 7], 5))
print(seq_search_ordered([1, 2, 3, 4, 5, 6, 7], 8))
