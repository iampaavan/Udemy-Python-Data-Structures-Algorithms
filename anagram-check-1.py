def anagram(s1, s2):
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    return sorted(s1) == sorted(s2)


s1 = 'dog'
s2 = 'god'
s3 = ''
s4 = ''
print(anagram(s1, s2))
print(anagram(s3, s4))