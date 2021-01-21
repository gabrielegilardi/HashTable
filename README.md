# Hash Table Data Structure

Hash table class implementation using lists and double-linked lists.

## Reference

[Problem Solving with Algorithms and Data Structures](runestone.academy/runestone/books/published/pythonds/index.html), by Miller and Ranum.

Prime numbers on [GeekforGeeks](geeksforgeeks.org/prime-numbers) and on [Wikipedia](en.wikipedia.org/wiki/Prime_number).

## File

`HashTable.py` Hash table class and prime number helper functions.

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
find_prime()        find the closest (higher) prime number to a given value.
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

- The double-linked list class is from [here](github.com/gabrielegilardi/LinkedLists.git)

## Examples

Examples of usage are at the end of the file.
