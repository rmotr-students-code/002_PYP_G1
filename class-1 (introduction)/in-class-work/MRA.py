def create_queue(name):
    name = []
    return name

def add_element_to_queue(queue, element, priority):
    position = 0
    for item in queue:
        current_item_priority = item[1]
        if current_item_priority < priority:
            pass
        elif current_item_priority >= priority:
            queue.insert(position, (element, priority))
        position += 1
    queue.insert(position, (element, priority))

x = []
add_element_to_queue(x,'a',3)
add_element_to_queue(x,'b',1)
print x


