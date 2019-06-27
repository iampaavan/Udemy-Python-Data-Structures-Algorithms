def quick_sort(array):

    quick_sort_help(array, 0, len(array) - 1)

    return array


def quick_sort_help(array, first, last):

    if first < last:

        splitpoint = partition(array, first, last)

        quick_sort_help(array, first, splitpoint-1)
        quick_sort_help(array, splitpoint+1, last)


def partition(array, first, last):

    pivot_value = array[first]
    left_mark = first + 1
    right_mark = last

    done = False

    while not done:

        while left_mark <= right_mark and array[left_mark] <= pivot_value:
            left_mark += 1

        while right_mark >= left_mark and array[right_mark] >= pivot_value:
            right_mark -= 1

        if right_mark < left_mark:
            done = True

        else:
            temp = array[left_mark]
            array[left_mark] = array[right_mark]
            array[right_mark] = temp

    temp = array[first]
    array[first] = array[right_mark]
    array[right_mark] = temp

    return right_mark


print(quick_sort([10, 2, 3, 5, 8, 9, 6, 4]))