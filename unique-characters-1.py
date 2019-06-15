def unique_characters(string):
    return len(set(string)) == len(string)


print(unique_characters('ABCD'))
print(unique_characters('AAAAA'))
