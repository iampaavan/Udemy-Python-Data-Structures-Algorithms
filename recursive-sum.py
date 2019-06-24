def recursive_sum(number):

    # Edge Case
    if number == 0:
        return number

    else:
        return number + recursive_sum(number - 1)


print(recursive_sum(0))
print(recursive_sum(4))
print(recursive_sum(100))