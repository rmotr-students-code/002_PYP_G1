# 5) Update all the names containing the string "po" to lowercase.

import re

def replace_po():
    with open('names_5.txt', 'r+') as f:
        mylist = []

        for line in f.readlines():
            if re.search(r'po', line, re.I) is not None:
                mylist.append(line.lower())
            else:
                mylist.append(line)

        f.seek(0, 0)
        f.truncate()

        for line in mylist:
            f.write(line)

replace_po()
