import string

def toJadenCase(string):
    words = string.split()
    retWords = []
    for word in words:
        if not word[0].isupper():
            retWords.append(word.capitalize())
        else:
            retWords.append(word)
    return ' '.join(map(str, retWords))

print("How can mirrors be real if our eyes aren't real")
print(toJadenCase("How can mirrors be real if our eyes aren't real"))