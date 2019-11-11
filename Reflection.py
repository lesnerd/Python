
class SampleClass:
    def __init__(self, val):
        self.val = val

    def getVal():
        return self.val

    def printDavid():
        return "David"

class Plant: pass                        # Dummy class
class Tree(Plant): pass                  # Dummy class derived from Plant
tree = Tree()                            # A new instance of Tree class

print("============== Tree and Plant examples ==============")
print(isinstance(tree, Tree))             # True
print(isinstance(tree, Plant))            # True
print(isinstance(tree, object))           # True
print(type(tree) is Tree)                 # False
print(type(tree).__name__ == "instance")  # True
print(tree.__class__.__name__ == "Tree")  # True

print("============== Simple examples ==============")
print(type(SampleClass))
#print(type(SampleClass).values())
print(type(str()))
print(type(int))
print(type(1.5))
print(type(3).__name__ == "int")
print(type('Hello').__name__ == "str")
print(dir(SampleClass))
print("==== Blah ====")
for property, value in vars(SampleClass).iteritems():
    print(property, ": ", value)

