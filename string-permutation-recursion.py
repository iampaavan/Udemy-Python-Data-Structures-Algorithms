from itertools import permutations


def permute(string):

    output = []
    # Edge Case
    if len(string) == 1:
        output.append(string)

    else:

        for index, letter in enumerate(string):
            for permutation in permute(string[:index] + string[index+1:]):
                output += [letter+permutation]

    return output


print(permute('abc'))
print(permute('abcd'))
print(permute('a'))


def string_permutation(string):

    my_list = []

    output = permutations(string)

    for i in output:
        my_list.append(''.join(i))

    return my_list


print(string_permutation('abc'))