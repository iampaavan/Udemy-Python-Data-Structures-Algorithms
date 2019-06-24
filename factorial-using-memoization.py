def factorial(number):

    fact_memo = dict()

    if number < 2:
        return 1

    if number not in fact_memo:
        fact_memo[number] = number * factorial(number - 1)

    return fact_memo[number]


print(factorial(5))
