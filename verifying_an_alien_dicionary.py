'''
In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographically in this alien language.

Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
Example 2:

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
Example 3:

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).

Asked by Facebook. [Easy]
'''

def is_alien_sorted(words, order):
    indexed_order = {c: i for i, c in enumerate(order)}
    for i in range(len(words) - 1):
        word1, word2 = words[i], words[i + 1]

        for j in range(len(word1)):
            if j == len(word2):
                return False
            if word1[j] != word2[j]:
                if indexed_order[word1[j]] > indexed_order[word2[j]]:
                    return False
                break

    return True

print(is_alien_sorted(["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz"))
print(is_alien_sorted(["word","world","row"], "worldabcefghijkmnpqstuvxyz"))
print(is_alien_sorted(["apple","app"], "abcdefghijklmnopqrstuvwxyz"))