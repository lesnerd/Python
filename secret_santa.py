# Secret santa (gamad anak)


import random

give =["a", "b", "c"]
# a -> c
# b -> A
# c -> b

# a -> b
# b -> a
# c -> 

def get_game(a):
    pairs = dict()
    taken = dict()
    for i,v in enumerate(a):
        gives = random.randint(0, len(a)-1)
        while gives == i or a[gives] in taken:
            if len(taken) == len(a) - 1 and v not in taken:
                replace = random.choice(list(pairs.items()))
                pairs[v] = replace[1]
                pairs[replace[0]] = v
                return pairs
            gives = random.randint(0, len(a)-1)
        pairs[v] = a[gives]
        taken[a[gives]] = 0
    
    return pairs


print(get_game(give))