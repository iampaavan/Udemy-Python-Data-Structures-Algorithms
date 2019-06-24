def reverse(string):

    rev = ''

    for i in reversed(string):
        rev += i

    return rev


print(reverse('abc'))


def reverse_string(string):

    if len(string) <= 1:
        return string

    return reverse_string(string[1:]) + string[0]


print(reverse_string('abc'))


def reverse_number(number):

    rev = 0
    while number:
        remainder = number % 10
        rev = rev * 10 + remainder
        number = number // 10

    return rev


print(reverse_number(321))


def reverse_number_recursion(number):

    if len(number) <= 1:
        return number

    return reverse_number_recursion((number[1:])) + number[0]


print(reverse_number_recursion('321'))
