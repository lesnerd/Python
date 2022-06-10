'''
This problem was asked Microsoft.
Using a read7() method that returns 7 characters from a file, implement readN(n) which reads n characters.

For example, given a file with the content “Hello world”, three read7() returns “Hello w”, “orld” and then “”.
'''

class Solution(object):
    def __init__(self, content):
        self.content = content
        # save file pointer
        self.offset = 0
        # cache remaining
        self.buffer = ''

    def readN(self, n):
        while len(self.buffer) < n:
            piece = self._read7()
            if not piece:
                break
            self.buffer += piece
        n_chars = self.buffer[:n]
        self.buffer = self.buffer[n:]
        return n_chars

    def _read7(self):
        start = self.offset
        end = min(self.offset+7, len(self.content))
        self.offset = end
        return self.content[start:end]

sol1 = Solution('Hello world')
assert sol1.readN(8) == 'Hello wo'
assert sol1.readN(8) == 'rld'
assert sol1.readN(8) == ''

sol2 = Solution('Hello world')
assert sol2.readN(4) == 'Hell'
assert sol2.readN(4) == 'o wo'
assert sol2.readN(4) == 'rld'