def bubble_sort(array):

    for n in range(len(array)-1, 0, -1):

        for i in range(n):

            if array[i] > array[i+1]:
                temp = array[i]
                array[i] = array[i+1]
                array[i+1] = temp

    return array


print(bubble_sort([5, 2, 3, 1, 6, 4]))
