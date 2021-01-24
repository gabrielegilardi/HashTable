# Hash Table and Dictionary Data Structures

Hash table and dictionary class implementation using lists and double-linked lists.

## References

[Problem Solving with Algorithms and Data Structures](https://runestone.academy/runestone/books/published/pythonds/index.html), by Miller and Ranum.

Prime numbers on [GeekforGeeks](https://www.geeksforgeeks.org/prime-numbers/) and on [Wikipedia](https://en.wikipedia.org/wiki/Prime_number).

## Files

`HashTable.py` Hash table class implementation using lists and double-linked lists.

```python
"""
HashTable Class:
size            Size of the hash table.
hashing         Hashing method.
collision       Collision resolution method.
c               Factor in the multiplication hashing method.
digit           Number of digits in the folding hashing method.
table           Hash table
n_slots         Number of occupied slots.
n_items         Number of items in the table
state           State table to track deleted/never deleted slosts.
skip            Skip value in the rehashing collision resolution method.
fact            Factor in the quadratic collision resolution method.
__init__()      Initializes the hash table.
__repr__()      Returns stats and info about the hash table.
load_factor()   Returns the load factor of the hash table.
items()         Returns a list of tuples with all items in the hash table.
convert()       Returns the integer value associated with an item.
hash_index()    Returns the hash (slot) index given an integer value.
insert()        Inserts an item in the hash table.
delete()        Deletes an item from the hash table.
search()        Searches an item in the hash table.
clear()         Removes all items from the hash table.

Prime number functions:
is_prime_det()      Deterministically check if a given value is a prime number.
is_prime_prob()     Probabilistically check if a given value is a prime number.
find_prime()        Find the closest (higher) prime number to a given value.
"""
```

- Written and tested in Python 3.8.5.

- Hashing methods: folding, multiplication, remainder.

- Collision resolution methods: rehashing, quadratic, chaining.

- Items converted to integer using the ordinal value and positional weight.

- Rehashing method can work with any skip value, quadratic method can work
  with any multiplicative factor.

- Possible to pass an initial list of values when creating the hash table.

- Possible to have duplicate values (search will return the first occurrence).

`Dictionary.py` Dictionary class implementation using a hash table.

```python
"""
Dict Class:
size            Size of the dictionary.
skip            Skip value in the rehashing collision resolution method.
n_items         Number of items (pair key-values) in the dictionary.
keys            Hash table with the dictionary keys.
values          List with the dictionary values.
__init__()      Initializes the dictionary.
__repr__()      Returns info about the dictionary.
is_empty()      Checks if the dictionary is empty or not.
get_items()     Returns a list of all items in the dictionary.
get_keys()      Returns a list of all keys in the dictionary.
get_value()     Returns a list of all values in the dictionary.
put()           Adds a new item to the dictionary.
get()           Returns the value associated with a key.
search()        Searches the dictionary for a key.
remove()        Removes an item from the dictionary.
clear()         Removes all items from the dictionary.
"""
```

- Written and tested in Python 3.8.5.

- Hash table uses 'remainder' as hashing method and 'rehashing' as collision
  resolution method.

- Possible to pass an initial list of items when creating the dictionary.

- Possible to define the skip value to be used in the hash table.

- Easy to resize the dictionary and change the skip value (see example).

- Methods in this class has been written trying to use the HashTable class as
  is, and thus they may not be the best in term of efficiency.

`DoubleLinkedList.py` Double-linked list class implementation using a double-list node class (see [here](github.com/gabrielegilardi/LinkedLists.git)).

## Examples

Examples of usage are at the end each file.
