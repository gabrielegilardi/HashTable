# Basic Data Structures

Stack, queue, priority queue, and binary heap data structures.

## Reference

[Problem Solving with Algorithms and Data Structures](https://runestone.academy/runestone/books/published/pythonds/index.html), by Miller and Ranum.

## Files

`Stack.py` Stack data structure using lists.

```python
"""
__init__()      Initializes the stack.
__repr_()       Returns the string representation of the stack.
is_empty()      Checks if the stack is empty.
push()          Adds one item to the top of the stack.
pop()           Returns and removes the item at the top of the stack.
peek()          Returns the item at the top of the stack.
reverse()       Reverses the stack.
clear()         Removes all items from the stack.
"""
```

`Queue.py` Queue data structure using lists.

```python
"""
__init__()      Initializes the priority queue.
__repr_()       Returns the string representation of the queue.
is_empty()      Checks if the queue is empty.
enqueue()       Adds one item to the back of the queue.
dequeue()       Returns and removes the item at the front of the queue.
peek()          Returns the item at the front of the queue.
reverse()       Reverses the queue.
clear()         Removes all items from the queue.
"""
```

`PriorityQueue.py` Priority queue (max/min) data structure using lists.

```python
"""
__init__()      Initializes the priority queue.
__repr_()       Returns the string representation of the priority queue.
is_empty()      Checks if the priority queue is empty.
put()           Adds one item to the priority queue.
get()           Returns and removes the item at the front of the priority queue.
peek()          Returns the item at the front of the priority queue.
reverse()       Reverses the priority queue (from min to max and viceversa).
clear()         Removes all items from the priority queue.
"""
```

`BinaryHeap.py` Binary heap (max/min) data structure using lists.

```python
"""
__init__()      Initializes the binary heap.
__repr_()       Returns the string representation of the binary heap.
is_empty()      Checks if the binary heap is empty.
swap_up()       Swaps an item up to preserve the binary heap property.
swap_down()     Swaps an item down to preserve the binary heap property.
put()           Adds one item to the binary heap.
get()           Returns and removes the item at the root of the binary heap.
peek()          Returns the item at the root of the binary heap.
reverse()       Reverses the binary heap (from min to max and viceversa).
clear()         Removes all items from the binary heap.
"""
```

## Examples and Notes

See each file.
