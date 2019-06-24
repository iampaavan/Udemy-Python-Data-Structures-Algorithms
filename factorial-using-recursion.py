def factorial(number):

    fact = 1

    # Edge Case
    if number == 0 or number == 1:
        return fact

    return number * factorial(number - 1)


print(factorial(5))
print(factorial(0))
print(factorial(1))
