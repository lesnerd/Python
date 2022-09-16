'''
This problem was asked by Microsoft.

Given a dictionary of words and a string made up of those words (no spaces), return the original sentence in a list. If there is more than one possible reconstruction, return any of them. If there is no possible reconstruction, then return null.

For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox", you should return ['the', 'quick', 'brown', 'fox'].

Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond", return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].
'''

# def wordBreak(s, wordDict) -> bool:
#     dp = [True] + [False] * len(s)
#     for i in range(1, len(s) + 1):
#         for word in wordDict:
#             if s[:i].endswith(word):
#                 dp[i] |= dp[i-len(word)]
#     return dp[-1]

# print(wordBreak("thequickbrownfox", ["the", "quick", "brown", "fox"]))


def wordBreak(s, wordDict) -> bool:
    ret = []
    for i in range(0, len(s)):
        for word in wordDict:
            if s[i:i+len(word)].endswith(word):
                ret.append(s[i:i+len(word)])
                break
    return ret

print(wordBreak("thequickbrownfox", ["the", "quick", "brown", "fox"]))