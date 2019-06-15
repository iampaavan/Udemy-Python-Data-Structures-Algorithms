def large_cont_sum(array):

    # Edge Case Check
    if len(array) == 0:
        return 0

    current_sum = array[0]
    maximum_sum = array[0]

    for number in array[1:]:

        current_sum = max(current_sum + number, number)
        maximum_sum = max(current_sum, maximum_sum)

    return maximum_sum


print(large_cont_sum([1, 2, -1, 3, 4, 10, 10, -10, -1]))
