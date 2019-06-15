def array_pairs(array, target):

    sums = []
    hashtable = {}

    for number in array:
        sum_minus_element = target - number

        if sum_minus_element in hashtable:
            sums.append((number, sum_minus_element))

        hashtable[number] = number

    print(f"No of pairs: {len(sums)}")
    return sums


print(array_pairs([1, 3, 2, 2], 4))