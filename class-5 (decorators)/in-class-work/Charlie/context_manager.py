class ContextManager(object):
    
    def __enter__(self):
        print("So the context manager starts with this.")

    def __exit__(self, type, value, traceback):
        print("And it will ALWAYS end with this.")
    
with ContextManager():
    
    print("So this block runs AFTER the __enter__ runs.")
    raise NotImplementedError
    print("So this block runs AFTER the __enter__ runs. SECOND ONE")
    