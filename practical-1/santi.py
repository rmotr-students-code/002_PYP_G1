# 'a', 3
# 'g', 0
# 'd', 1
# 'z', 1



# data structure looks like queue = [(item, priority), (item2, priority)] 
def add_element_to_queue(queue, element, priority):
    # queue = [('g', 0), ('a', 3)]
    # element = 'd'
    # priority = 1
    position = 0
    for item in queue:
        # position = 1
        # item ('a', 3)
        # current_item_priority == 3
        current_item_priority = item[1]
        if current_item_priority < priority:
            pass
        elif current_item_priority >= priority:
            queue.insert(position, (element, priority))
        position += 1

    # this point
    # position == 0
    queue.insert(position, (element, priority))





# [('g', 0), ('z', 1), ('d', 1), ('a', 3)]
q = []
add_element_to_queue(q, 'a', 3)
add_element_to_queue(q, 'g', 0)
add_element_to_queue(q, 'd', 1)
add_element_to_queue(q, 'z', 1)


assert q == [('g', 0), ('z', 1), ('d', 1), ('a', 3)]

def next_element(queue):
    # returns (and removes) the next element in the queue.
    pass
