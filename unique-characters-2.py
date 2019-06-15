def unique_characters(string):

    chars = set()

    for letter in string:

        if letter in chars:
            return False

        else:
            chars.add(letter)

    return True


print(unique_characters('AAAAAAAAA'))
print(unique_characters('ABCD'))
