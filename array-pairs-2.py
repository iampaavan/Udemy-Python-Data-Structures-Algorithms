def array_pairs(array, target):

    # Edge Case Check
    if len(array) < 2:
        return "No Pairs."

    seen = set()
    output = set()

    for number in array:

        sum_minus_element = target - number

        if sum_minus_element not in seen:
            seen.add(number)

        else:
            output.add((min(sum_minus_element, number), max(sum_minus_element, number)))

    print(f"No of Pairs: {len(output)}")
    print('\n'.join(map(str, output)))


array_pairs([1, 3, 2, 2], 4)