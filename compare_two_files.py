'''
compare 2 strings and print the differences to 3 different arrays:
1. added lines
2. changed lines
3. removed lines
'''

import difflib

def compare_two_files(f1_lines, f2_lines):    
    d = difflib.Differ()
    diff = list(d.compare(f1_lines, f2_lines))
    
    added = []
    changed = []
    removed = []
    for line in diff:
        if line.startswith('+'):
            added.append(line)
        elif line.startswith('-'):
            removed.append(line)
        elif line.startswith('?'):
            changed.append(line)
    
    return added, changed, removed

def compare_two_files_manual(content1, content2):
    if content1 == content2:
        return [], [], [], []
    if content1 == '':
        return content2.split('\n'), [], [], []
    if content2 == '':
        return [], [], [], []
    lines1 = content1.split('\n')
    lines2 = content2.split('\n')
    
    added = []
    changed = []
    removed = []
    diff = []
    for i in range(len(lines1)):
        if i < len(lines2):
            if lines1[i] != lines2[i]:
                changed.append(lines1[i])
                changed.append(lines2[i])
                break
            else:
                diff.append(lines1[i])
        else:
            removed.append(lines1[i])
    
    # add the rest of the lines from the second file
    for i in range(len(lines2)):
        if i >= len(lines1):
            added.append(lines2[i])
    
    return added, changed, removed, diff


f1 = """id,name,year of birth
1,albert einstein,1879
2,isaac newton,1643
3,marie curie,1867
4,galilée,1564"""

f2 = """id,name,year of birth
1,Albert einstein,1879
2,isaac newton,1643
4,galileo,1564
5,stephen hawking,1942"""

added, changed, removed, diff = compare_two_files_manual(f1, f2)


# added, changed, removed = compare_two_files(f1.split('\n'), f2.split('\n'))
print('Added lines:')
for line in added:
    print(line)
print('Changed lines:')
for line in changed:
    print(line)
print('Removed lines:')
for line in removed:
    print(line)
print('All lines:')