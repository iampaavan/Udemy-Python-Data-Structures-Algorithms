def insertion_sort(array):

    for i in range(1, len(array)):

        current_value = array[i]
        position = i

        while position > 0 and array[position-1] > current_value:

            array[position] = array[position-1]
            position = position - 1

        array[position] = current_value

    return array


print(insertion_sort([54, 10, 36, 25, 89, 57, 15, 30]))
