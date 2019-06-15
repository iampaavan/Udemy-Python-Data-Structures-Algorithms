def reverse_string(string):

    words = []
    length = len(string)
    spaces = [' ']

    i = 0

    while i < length:

        if string[i] not in spaces:

            words_start = i

            while i < length and string[i] not in spaces:

                i += 1

            words.append(string[words_start:i])

        i += 1

    return " ".join(reversed(words))


print(reverse_string('       Hello John           how are you              '))
