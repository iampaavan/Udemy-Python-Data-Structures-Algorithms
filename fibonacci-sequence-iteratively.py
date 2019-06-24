def fib_iter(number):

    a, b = 0, 1

    for i in range(number):
        a, b = b, a+b
        print(a, end=', ')

    print()
    return a


print(fib_iter(10))
print(fib_iter(9))
