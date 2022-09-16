'''
Given a list of string 'words' from an alien dictionary where the string in works re sorted lexicographically by the rules of this new language. 
Return a string of the unique letters in the new alien language sorted in lexicographical increasing order by the new language's rules. If there is no solution, return "".
If there are multiple solutions, return any of them.

Example 1:
Input: words = ["wrt","wrf","er","ett","rftt"]
Output: "wertf"

Example 2:
Input: words = ["z","x"]
Output: "zx"

[Hard]

Notes:
chars of a word not in order, the words are in order, 
find adjacency list of each unique char by iterating through adjacent words and finding first chars that are different, run topsort on graph and do loop detection;
'''

def alien_order(words):
    # adjecency_list = { c:set() for word in words for c in word }

    adjecency_list = {}
    for word in words:
        for char in word:
            adjecency_list[char] = set()

    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i + 1]
        minlen = min(len(w1), len(w2))
        if w1[:minlen] == w2[:minlen] and len(w1) > len(w2):
            return ""
        for j in range(minlen):
            if w1[j] != w2[j]:
                adjecency_list[w1[j]].add(w2[j])
                break

    visited = {}
    res = []
    for char in adjecency_list:
        if dfs(char, visited, res, adjecency_list):
            return ""
    res.reverse()
    return "".join(res)

def dfs(node, visited, res, adj):
    if node in visited: # detect loop if the return value is true
        return visited[node]

    visited[node] = True
    for neighbor in adj[node]:
        if dfs(neighbor, visited, res, adj): # detect loop if the return value is true
            return True

    visited[node] = False
    res.append(node)


print(alien_order(["wrt", "wrf", "er", "ett", "rftt"]))