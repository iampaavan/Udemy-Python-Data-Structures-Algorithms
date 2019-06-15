def compress(string):

    r = ''
    l = len(string)

    if l > 0:
        last = string[0]

    counter = 1

    i = 1

    # Edge Case
    if l == 0:
        return "No string to compress."

    if l == 1:
        return string + str(counter)

    while i < l:

        if string[i] == string[i - 1]:
            counter += 1

        else:
            r = r + string[i - 1] + str(counter)
            counter = 1

        i += 1

    r = r + string[i - 1] + str(counter)

    return r


print(compress('AAAAAABBBBBBBBBcccccccc'))
print(compress('AAB'))
print(compress('AAAABBBBCCCCCDDEEEE'))
print(compress(''))
print(compress('A'))

