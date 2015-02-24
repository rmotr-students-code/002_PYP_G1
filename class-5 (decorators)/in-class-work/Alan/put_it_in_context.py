class OuttaContext(object):
    def __enter__(self):
        print "beginning....!"
    
    def __exit__(self, *args):
        print "we're all finished."
        
    

with OuttaContext() as oc:
    print "in the beginning"
    raise ValueError
    print "in the end"
    