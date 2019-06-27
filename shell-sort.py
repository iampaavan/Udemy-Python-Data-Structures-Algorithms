def shell_sort(array):

    sublistcount = len(array) // 2

    while sublistcount > 0:

        for start in range(sublistcount):

            gap_insertion_sort(array, start, sublistcount)

        sublistcount = sublistcount // 2

    return array


def gap_insertion_sort(array, start, gap):

    for i in range(start+gap, len(array), gap):

        current_value = array[i]
        position = i

        while position >= gap and array[position-gap] > current_value:

            array[position] = array[position-gap]
            position = position-gap

        array[position] = current_value


print(shell_sort([54, 10, 36, 25, 89, 57, 15, 30]))
