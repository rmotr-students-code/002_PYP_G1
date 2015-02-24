# Assignments


### *mutability

What's the difference between a mutable and an immutable type? Why should I use one or the other?
Write the following two functions, both receiving a list of elements and a new elemnt to append at the end. The first one should be a mutable version and the second an immutable version.

Example mutable:

    l = [1, 2, 3]
    mutable_append(l, 'a')
    print(l)  # Should print [1, 2, 3, 'a']
    
Example immutable:

    l = [1, 2, 3]
    new_l = immutable_append(l, 'a')
    print(l)  # Should print [1, 2, 3]
    print(new_l)  # Should print [1, 2, 3, 'a']


### Average

Write a function that can either receive a list or different integer arguemnts and computes the Average:

Example:

    average(1, 5, 3, 2)  # 2.75
    average([1, 5, 3, 2]) # 2.75

### Pack

Write a function that receives an arbitrary amount of params and build a list with them.

Example:

    build_list(1, 5, "hello") == [1, 5, "hello"]

### Map squares

Write a function called squares that receives a list and returns the square of the elements. You MUST use the `map()`* function and lambdas.

Example:
    
    squares([1, 2, 3]) == [1, 4, 9]

### Map pows

Modify your previous function to receive one more argument "power" which should be optional (default to 2) that will be the power to raise each element on the list. Again, you MUST use `map()`* and lambdas.

    exponentiation([1, 2, 3], power=3) == [1, 8, 27]
    
### Square of evens

Write a function which receives a list of ints and returns a new list with the squares of the even numbers. You MUST use `map()`, `filter()`* and lambdas.

Example:

    square_of_evens([1,2,3,4,5,6,7,8,9,10]) == [4, 16, 36, 64, 100]

(*) map and filter are key functions in the functional paradigm. The Well known model MapReduce(http://en.wikipedia.org/wiki/MapReduce) invented by Google uses those function as foundational parts.

### Min max
Given a list of integers return the largest and the smallest values.

### Calculator based on functions

Define a couple of mathematical operation functions. For example:

    sum(1, 5, 6)      # Should return 12
    sum(1, 3)         # Should return 4
    subtract(5, 2)    # Should return 3
    subtract(5, 2, 1) # Should return 2

Create a calculator that can take a function operation and a list of arguments to process:

    calculator(sum, 1, 5, 6)   # Should return 12
    #           ^ This is our previously defined `sum` function
    calculator(sum, 1, 3)      # Should return 4
    calculator(subtract, 5, 2) # Should return 3


### Calculator dict

Similar to our previous exercise, but the interface of the calculator is different:

    calculator('sum', 1, 5, 6)   # Should return 12
    #           ^ This is a String
    calculator('sum', 1, 3)      # Should return 4
    calculator('subtract', 5, 2) # Should return 3

It now accepts a string as the operation name.

IMPORTANT: You can't use if statements. You have to use a dictionary.