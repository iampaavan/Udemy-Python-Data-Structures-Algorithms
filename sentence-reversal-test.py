def reverse_sentence(string):

    # Remove white space
    return ' '.join(reversed(string.split()))


print(reverse_sentence('This is the best         asd'))


def sentence(string):
    return ' '.join(string.split()[::-1])


print(sentence('This is the best'))