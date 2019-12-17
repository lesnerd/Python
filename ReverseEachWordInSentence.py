def reverseWordInSentence(sentence):
    if sentence is None:
        return None

    words = sentence.split(" ")

    newWords = [word[::-1] for word in words]

    return " ".join(newWords)

def reverseTheWholeString(sentence):
    if sentence is None:
        return None

    newWord = ''
    for i in range(len(sentence) - 1, -1, -1):
        newWord = newWord + sentence[i]
    return newWord

def reverseTheWordsOnly(sentence):
    if sentence is None:
        return None

    words = sentence.split(" ")
    return " ".join(words[::-1])

print(reverseWordInSentence("I am trying to solve this problem."))
print(reverseTheWholeString("This is microsoft")) # Should print: tfosorcim si sih
print(reverseTheWordsOnly("This is microsoft")) # Should print: microsoft is this