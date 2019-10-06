import string

def accum(s):
    index = 1
    ret = ''
    for c in range(len(s)):
        word = s[c].upper()
        for i in range(index-1):
            word +=s[c].lower()
        index +=1
        if c != len(s)-1:
            ret += word + '-'
        else:
            ret += word
        word = ''
    return ret

print(accum("ZpglnRxqenU"))
print("Z-Pp-Ggg-Llll-Nnnnn-Rrrrrr-Xxxxxxx-Qqqqqqqq-Eeeeeeeee-Nnnnnnnnnn-Uuuuuuuuuuu")
print(accum("NyffsGeyylB"))
print("N-Yy-Fff-Ffff-Sssss-Gggggg-Eeeeeee-Yyyyyyyy-Yyyyyyyyy-Llllllllll-Bbbbbbbbbbb")
