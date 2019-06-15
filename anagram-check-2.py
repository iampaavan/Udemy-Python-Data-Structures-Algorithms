def anagram(string1, string2):

    string1 = string1.replace(" ", "").lower()
    string2 = string2.replace(" ", "").lower()

    # Edge Case Check
    if len(string1) != len(string2):
        return False

    counter = {}

    for letter in string1:

        if letter in counter:
            counter[letter] += 1

        else:
            counter[letter] = 1

    for letter in string2:

        if letter in counter:
            counter[letter] -= 1

        else:
            counter[letter] = 1

    for item in counter:
        if counter[item] != 0:
            return False

    return True


string1 = 'clint eastwood'
string2 = 'old west action'

print(anagram(string1, string2))