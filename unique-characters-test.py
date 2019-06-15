from collections import defaultdict


def unique_characters(strings):

    # Edge Case
    if len(strings) == 0:
        return "String empty. No unique characters"

    d = defaultdict(int)

    for letter in strings:

        if letter in d:
            d[letter] += 1

        else:
            d[letter] = 1

    for key, value in d.items():

        if value > 1:
            return False

        return True


print(unique_characters('AAAAAAAAAAA'))
print(unique_characters('ABCD'))
print(unique_characters(''))
print(unique_characters('AaBb'))
