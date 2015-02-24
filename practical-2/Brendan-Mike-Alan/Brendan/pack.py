'''
### Pack

Write a function that receives an arbitrary amount of params and build a list with them.

Example:

    build_list(1, 5, "hello") == [1, 5, "hello"]
'''

def build_list(*args):
    return [x for x in args]

print build_list(1, 5, 'hello')