from collections import defaultdict
import operator


def string_compression(string):

    d = defaultdict(int)
    result = ''

    # Edge Case
    if len(string) == 0:
        return "No string to compress."

    for letter in string:

        if letter in d:
            d[letter] += 1

        else:
            d[letter] = 1

    for key, value in sorted(d.items(), key=operator.itemgetter(0)):
        result += key + str(value)

    return result


print(string_compression('CCCCCCDDDDDAAAAAAAA'))
print(string_compression('AAB'))
print(string_compression('AAAABBBBCCCCCDDEEEE'))
print(string_compression(''))
print(string_compression('A'))

