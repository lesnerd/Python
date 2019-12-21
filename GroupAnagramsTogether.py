def groupAnagrams(arr):
    if arr is None:
        return [[]]
    
    dic = dict()
    for word in arr:
        if ''.join(sorted(word)) in dic:
            dic[''.join(sorted(word))].append(word)
        else:
            dic[''.join(sorted(word))] = [word]

    ret = []
    for key in dic:
        ret.append(dic[key])

    return ret





print(groupAnagrams(['eat', 'ate', 'apt', 'pat', 'tea', 'now']))
# groupAnagrams(['eat', 'ate', 'apt', 'pat', 'tea', 'now'])