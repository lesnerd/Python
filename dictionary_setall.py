'''
Create a new kind of dictionary that can do all the operations that a regular dictionary can do, 
but also has a method called set_all that takes a single argument and sets all the values in the dictionary to that value in O(1).
'''

class DictionarySetAll:
    def __init__(self):
        self.dict = {}
        self.set_all_val = None
        self.set_all_flag = False

    def __getitem__(self, key):
        if self.set_all_flag:
            return self.set_all_val
        return self.dict[key]

    def __setitem__(self, key, value):
        self.set_all_flag = False
        self.dict[key] = value

    def set_all(self, value):
        self.set_all_flag = True
        self.set_all_val = value

    def __str__(self):
        return str(self.dict)

    def __repr__(self):
        return str(self.dict)