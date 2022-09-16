'''
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.

Example 1:
Input: text = "nlaebolko"
Output: 1

Example 2:
Input: text = "loonbalxballpoon"
Output: 2

Example 3:
Input: text = "leetcode"
Output: 0
'''

def max_number_of_balloons(text):
    balloon = 'balloon'
    balloon_dict = {c: 0 for c in balloon}
    for c in text:
        if c in balloon_dict:
            balloon_dict[c] += 1
    balloon_dict['l'] //= 2
    balloon_dict['o'] //= 2
    return min(balloon_dict.values())

print(max_number_of_balloons("nlaebolko"))
print(max_number_of_balloons("loonbalxballpoon"))
print(max_number_of_balloons("leetcode"))

# Use if 2 dictionaries 1 for 'balloon' and the second for the actual text.
def maxNumberOfBalloons(text):
    if text is None:
        return 0
    if len(text) < 7:
        return 0
    balloonOrg = {'b': 1, 'a': 1, 'l': 2, 'o': 2, 'n': 1 }
    balloonCnt = {'b': 0, 'a': 0, 'l': 0, 'o': 0, 'n': 0 }
    for c in text:
        if c in balloonCnt:
            balloonCnt[c] += 1
    res = len(text)
    for c in balloonOrg:
        res = min(res, balloonCnt[c] // balloonOrg[c])
        
    return res

print(maxNumberOfBalloons("nlaebolko"))
print(maxNumberOfBalloons("loonbalxballpoon"))
print(maxNumberOfBalloons("leetcode"))