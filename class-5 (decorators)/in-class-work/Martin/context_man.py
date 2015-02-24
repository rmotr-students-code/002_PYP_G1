class MartysContextManager(object):
    def __enter__(self):
        print("Marty's special header")
        
    def __exit__(self, type, value, traceback):
        print("Marty's Special signature")
        
with MartysContextManager():
    #raise NotImplemented()
    print("Wrap me with Marty goodness")
    
    
    