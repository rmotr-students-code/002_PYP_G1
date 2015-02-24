# 4) Sort the file by name in an ascendent way.

def sort_names():
    with open('names_4.txt', 'r+') as f:

        lines = f.readlines()
        f.seek(0,0)
        f.truncate()

        whole_line = []

        for line in lines:
            whole_line.append(line)

        # The last element in the list was writing on the same line as the previous entry when ordered. Manually put in
        # a new line
        whole_line[-1] = '{} \n'.format(whole_line[-1])

        for line in sorted(whole_line):
            f.write(line)


sort_names()




            

