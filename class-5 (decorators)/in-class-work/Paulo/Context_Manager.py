"""Example of Context Manager"""

"""Example of Context Manager"""

class MyContextManager(object):

    def __init__(self, file_name):
        self.file_name = file_name

    def __enter__(self):
        print("Warming Up")

    def opens_file(self):
        with open(self.file_name) as f:
            f.write('Tight, Tight, Yeah!')
        return self.file_name

    def __exit__(self, type, value, traceback):
        print ("This is now complete")

with MyContextManager('testing.txt') as filetesting:
    print('this is the middle')

    #raise ValueError
