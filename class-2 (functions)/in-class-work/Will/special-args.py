# ## function using special *args and **kwargs arguments.
def mult(*args):
   print args
mult(4, 5, 2)

def two(**kwargs):
   print kwargs 
   
two(v=1, x=2)