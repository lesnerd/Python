def get_middle(s):
    size = len(s)
    size = int((size / 2) -1)
    if len(s) % 2 == 0: # Even
        return s[size:size+2]
    else: # Odd
        return s[size+1]


print(get_middle("test"))
print(get_middle("testing"))
print(get_middle("middle"))
#print(get_middle("A"))
#print(get_middle("of"))