def reverseWordInSentence(sentence):
    if sentence is None:
        return None

    words = sentence.split(" ")

    newWords = [word[::-1] for word in words]

    return " ".join(newWords)



print(reverseWordInSentence("I am trying to solve this problem."))