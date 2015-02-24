def create_queue(queue):
    queue = {}
    return queue

def add_element_to_queue(queue, element, priority):
    queue[element] = priority
    
    
def next_element(queue):
    
    lowest =min(queue.items(), key=lambda x: x[1])
    #so now for the pop, is that right?
    print lowest[0]
    del queue[lowest[0]]
    
    
    
    #when i run this:
    '''q = {"a":12,"b":2,"d":4}
    x = min(q.items(), key=lambda x: x[1])
    print x
    '''
    #It gives the smallest key/value
    # a = queue.pop(0) removes element at index 0 and saves it to var "a"
    #what does pop do? never seen it. ohhhhh Ok that was going to be my next question
    #im not really sure how to implement the pop
    
    '''
    lowest = None
    for activity in queue:
        if lowest is None or queue[activity] < lowest:
            lowest = queue[activity]
            
    print lowest
    '''

#so I can get the lowest value for the priority
#so:

# being 1 top priority
queue = create_queue("my_queue")
add_element_to_queue(queue, "clean my house", 5)
add_element_to_queue(queue, "study python", 8)
add_element_to_queue(queue, "visit my girlfriend", 2)



next_element(queue)  # should be "study python"
next_element(queue)
next_element(queue)
#returns 1


"""
# check this:
# might seems like black magic LOL haha. wasn't sure if there was a simple way to do it but I guess I'll try one of these
# great. thanks!
>>> d = {"a": 2, "b":0, "c":1}
>>> sorted(d.items(), key=lambda x: x[1])
[('b', 0), ('c', 1), ('a', 2)]
"""

# i found this as well: min(d, key=d.get)
