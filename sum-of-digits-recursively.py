def sum_of_digits(number):

    total = 0

    while number:

        r = number % 10
        number = number // 10
        total = total + r

    return total


print(sum_of_digits(4321))
print(sum_of_digits(9999))


def recursive_sum_of_digits(number):

    # Edge Case
    if len(str(number)) == 1:
        return number

    else:
        return number % 10 + recursive_sum_of_digits(number // 10)


print(recursive_sum_of_digits(4321))