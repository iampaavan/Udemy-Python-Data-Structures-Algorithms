def selection_sort(array):

    for fillslot in range(len(array)-1, 0, -1):

        position_of_max = 0

        for location in range(1, fillslot+1):

            if array[location] > array[position_of_max]:
                position_of_max = location

        temp = array[location]
        array[location] = array[position_of_max]
        array[position_of_max] = temp

    return array


print(selection_sort([5, 8, 3, 10, 1]))