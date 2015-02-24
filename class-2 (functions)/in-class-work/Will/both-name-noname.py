# ## function with both named and no-named arguments.
#    (named arguments must be on the right part of the argument list)

def both(first, last):
   return first + last

# both(5, last="string") can't add string and int
both('will', last='hoback')