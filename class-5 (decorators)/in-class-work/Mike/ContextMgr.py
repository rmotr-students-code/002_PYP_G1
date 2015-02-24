class MyContextManager(object):
    def __enter__(self):
        if sum(10,2) > 10:
            print("Those are some big numbers!")
        else:
            print("That's it?")

    def __exit__(self, type, value, traceback):
        print("Thank you for using Context Manager!")

def sum(a,b):
    print(a + b)

with MyContextManager():
    sum(10,2)

    