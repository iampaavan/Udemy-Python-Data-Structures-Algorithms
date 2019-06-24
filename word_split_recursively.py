def word_split(phrase, list_of_words, output=None):

    if output is None:
        output = []

    for words in list_of_words:
        if phrase.startswith(words):
            output.append(words)
            return word_split(phrase[len(words):], list_of_words, output)

    return output


print(word_split('themanran', ['the', 'man', 'ran']))
print(word_split('ilovedogsJohn', ['i', 'am', 'a', 'dogs', 'lover', 'love', 'John']))
print(word_split('themanran', ['clown', 'ran', 'man']))
