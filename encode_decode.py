'''
Description
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Please implement encode and decode

Wechat reply 【Google】 get the latest requent Interview questions. (wechat id : jiuzhang0607)

[Medium]

Example 1
Input: ["lint","code","love","you"]
Output: ["lint","code","love","you"]
Explanation:
One possible encode method is: "lint:;code:;love:;you"

Example 2
Input: ["we", "say", ":", "yes"]
Output: ["we", "say", ":", "yes"]
Explanation:
One possible encode method is: "we:;say:;:::;yes"
'''

class Codec:
    def encode(self, strs):
        if strs is None:
            return ""
        result = ""
        for s in strs:
            result += str(len(s)) + "#" + s
        return result


    def decode(self, str):
        if str is None or len(str) == 0:
            return []
        idx, result = 0, []
        while idx < len(str):
            while str[idx] != "#":
                idx += 1
            length = int(str[idx - 1])
            result.append(str[idx + 1: idx + 1 + length])
            idx += 1 + length
        return result


strs = ["lint","code","love","you"]
codec = Codec()
encoded = codec.encode(strs)
print(encoded)
result = codec.decode(encoded)
assert result == strs
print(result)