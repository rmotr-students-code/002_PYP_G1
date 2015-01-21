'''
# Here are the exercises I wrote. Just for reference
 
def times(string, times):
# Return the `string` str a certain amount of `times`
# times("Hello", 2) == "HelloHello"}
# How to have a default value for times?
    pass
 
 
def unpack_values(three_element_collection):
# Receive a collection with 3 elements, unpacks
# each element in a variable (first, second, third)
# and prints the three values on string.
# Prints an error if the collection doesn't have 3 elements.
    pass
 
 
def largest_item(collection):
# Receives a collection with ints and returns the lartest on
    
 
def count_evens(collection):
# Return the number of even ints in the given collection
    pass 
'''

#do you want to do 1 each?
#sounds good to me. Which eould you like to start with?

#cool i dont mind, ill do the 2nd

def times(string, times=1):
    return string * times

#I think for the default value, you can do times=2 in the arguments ==> def times(string, times=2)
#i'll take a stab at the third
def unpack_values(three_element_collection):
    if len(three_element_collection) == 3:
        first = three_element_collection[0]
        second = three_element_collection[1]
        third = three_element_collection[2]
        
        # PUT CODE HERE
        print(first, second, third)
    else:
        print "error"
    
    #what did we cheat? Yes i can hear you 
    

def largest_item(collection):
    largest = 0
    if isinstance(collection, list):
        for x in collection:
            if x > largest:
                largest = x
        return largest
    elif isinstance(collection, dict):
        for key, value in collection.items():
            #value = collection[key]  # You save this line
            if value > largest:
                largest = value
        return largest #so the problem was that i used value instead of key? Ok cool. can you check my question on line 73?
        
#it worked for the count evens one. Im confused, I don't understand what youre saying
# Brendan
# I was wondering how the for loop in the dict worked....
# I usually do this:

d = {'a': 1}
count = 0
for key, value in d.items():
    count += 1 #will that be 1 or 2? so does it count the key AND the value?
    #print (key, value)

#so is the first iteration 'a' and then the second 1. so count will be 2 in this case. 


#sorry
#np was confused for a second lol
#are you testing it on your own? Yes
def count_evens(collection):
    even_count = 0
    if isinstance(collection, list):
        for value in collection:
            if value % 2 == 0:
                even_count += 1
    elif isinstance(collection, dict):
        for value in collection:
            if collection[value] % 2 == 0:
                even_count += 1
        
        
    print even_count
    #I think that should work to check list or dict. but now we need to figure out how to find if the dict val is even
    #if we check the value rather than the key?
   #maybe...
   #try that
   
   #yeah , i'm really not sure however just brainstorming yeah me too lol
    #what part?
    # i saw a little box appear in my window
#like a chat box oh on the right click the "collaborate" tab and there is a group chat