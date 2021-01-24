"""
Hash Table Data Structure

Copyright (c) 2021 Gabriele Gilardi


Notes
-----
- Written and tested in Python 3.8.5.
- Hash table class implementation using lists and double-linked lists.
- Hashing methods: folding, multiplication, remainder.
- Collision resolution methods: rehashing, quadratic, chaining.
- Items converted to integer using the ordinal value and positional weight.
- Rehashing method can work with any skip value, quadratic method can work
  with any multiplicative factor.
- Possible to pass an initial list of values when creating the hash table.
- Possible to have duplicate values (search will return the first occurrence).
- is_prime_det() is a helper function to deterministically check if a given
  value is a prime number.
- is_prime_prob() is a helper function to probabilistically check if a given
  value is a prime number.
- find_prime() is a helper function to find the closest (higher) prime number
  to a given value using the deterministic or the probabiistic method.
- Examples of usage are at the end of the file.

References
----------
- "Problem Solving with Algorithms and Data Structures", by Miller and Ranum,
  @ runestone.academy/runestone/books/published/pythonds/index.html
- Prime numbers:
  @ geeksforgeeks.org/prime-numbers, en.wikipedia.org/wiki/Prime_number
- Double-linked list class:
  @ github.com/gabrielegilardi/LinkedLists.git

HashTable Class
---------------
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
"""


import random
import math

from DoubleLinkedList import DLL


def is_prime_det(n):
    """
    Returns <True> if <n> is a prime number, returns <False> otherwise. It
    uses an (optimized) deterministic method to guarantee that the result
    will be 100% correct.
    """
    # 2 and 3 are prime numbers
    if (n <= 3):
        return (n > 1)

    # Corner cases to speed up the next loop
    if (n % 2 == 0) or (n % 3 == 0):
        return False

    # Using (6k-1) and (6k+1) optimization
    i = 5
    while (i * i <= n):
        if (n % i == 0) or (n % (i + 2) == 0):      # Not a prime number
            return False
        i += 6

    return True


def is_prime_prob(n, k=5):
    """
    Returns <True> if <n> is a prime number, returns <False> otherwise. It
    uses a probabilistic method based on the Fermat little theorem. The
    probability of false positives can be reduced incresing <k>.

    - The probability of error when returns <True> is zero.
    - The probability of error when returns <False> is 2^-k.
    """
    def power(a, n, p):
        """
        Returns (a ^ n) % p using an iterative procedure to avoid overflow
        for large values of <n>.
        """
        res = 1
        a = a % p

        while (n > 0):

            if (n % 2):                 # If n is odd
                res = (res * a) % p
                n = n - 1

            else:                       # If n is even
                a = (a ** 2) % p
                n = n // 2

        return res % p

    # Corner cases
    if (n == 1 or n == 4):              # Not a prime number
        return False
    if (n == 2 or n == 3):              # Prime number
        return True

    # Repeat k-times for n > 4 and use Fermat little theorem to check if
    # it is NOT a prime number
    for i in range(k):
        a = random.randint(2, n-2)
        if (power(a, n-1, n) != 1):
            return False                # Not a prime number

    return True


def find_prime(value, method='det', k=5):
    """
    Returns the closest (higher) prime number to the given value.
    """
    n = value

    # Probabilistic method
    if (method == 'prob'):

        # Check if <value> is prime
        prime = is_prime_prob(n, k)

        # Find the first prime number after <value>
        while (not prime):
            n += 1
            prime = is_prime_prob(n, k)

    # Deterministic method
    else:

        # Check if <value> is prime
        prime = is_prime_det(n)

        # Find the first prime number after <value>
        while (not prime):
            n += 1
            prime = is_prime_det(n)

    return n


class HashTable:
    """
    Hash table class.
    """
    def __init__(self, size, init_list=None, hashing='remainder',
                 collision='chaining', c=0.618034, digit=2, param=1):
        """
        Initialize the hash table.

        Rehashing/quadratic methods need a state table to keep track of the
        slots that have been deleted in the past:

        state[slot] = False   -->   the slot has never been deleted
        state[slot] = True    -->   the slot has been deleted before
        """
        self.size = size
        self.hashing = hashing          # Folding, multiplication, remainder
        self.collision = collision      # Rehashing, quadratic, chaining
        self.c = c                      # Used in 'multiplication'
        self.digit = digit              # Used in 'folding'

        # Hashing table
        self.table = [None] * self.size
        self.n_slots = 0                # Number of occupied slots
        self.n_items = 0                # Numer of items in the table

        # For rehashing
        if (self.collision == 'rehashing'):
            self.state = [False] * self.size
            self.skip = param
            self.fact = 0               # Used in 'quadratic'

        # For quadratic
        elif (self.collision == 'quadratic'):
            self.state = [False] * self.size
            self.skip = 0               # Used in 'rehashing'
            self.fact = param

        # Add the initial list of values to the hash table
        if (init_list is not None):
            for item in init_list:
                self.insert(item)

    def __repr__(self):
        """
        Returns stats and info about the hash table.
        """
        return ("\nHashTable object \
                 \n- total size = {} \
                 \n- occupied slots = {} \
                 \n- number of items = {} \
                 \n- load factor = {:5.3f} \
                 \n- hashing method = {} \
                 \n- collision method = {}" \
                .format(self.size, self.n_slots, self.n_items,
                        self.load_factor(), self.hashing, self.collision))

    def load_factor(self):
        """
        Returns the load factor of the hash table.
        """
        return self.n_slots / self.size

    def items(self):
        """
        Returns a list of tuples with all items in the hash table. Slots with
        value <None> are not included in this list.

        For 'chaining' returns a list of tuples with the slot index and the
        corresponding double-linked list. For rehashing/quadratic returns a
        list of tuples with the slot index and the corresponding value.
        """
        items_list = [None] * self.n_slots
        idx = 0

        # If using chaining
        if (self.collision == 'chaining'):

            for slot in range(self.size):
                if (self.table[slot] is not None):
                    items_list[idx] = (slot, self.table[slot].nodes())
                    idx += 1

        # If using rehashing/quadratic
        else:

            for slot in range(self.size):
                if (self.table[slot] is not None):
                    items_list[idx] = (slot, self.table[slot])
                    idx += 1

        return items_list

    def convert(self, item):
        """
        Returns the integer value associated with an item.

        All items are first converted to strings and then associated to an
        integer number obtained adding the ordinal values of each character
        multiplied by its positional weight.
        """
        # Convert the item to a string
        str_item = str(item)

        # Add the ordinal value of each character using positional weight
        int_value = 0
        for i in range(len(str_item)):
            int_value += ord(str_item[i]) * (i + 1)

        return int_value

    def hash_index(self, int_value):
        """
        Returns the hash (slot) index of the specified integer value. Possible
        methods are folding, multiplication, and remainder.
        """
        # Folding
        if (self.hashing == 'folding'):
            str_value = str(int_value)
            n = len(str_value)
            slot = 0
            for i in range(0, n, self.digit):
                slot += int(str_value[i:min(i+self.digit, n)])
            slot = slot % self.size

        # Multiplication
        elif (self.hashing == 'multiplication'):
            slot = math.floor(self.size * math.modf(int_value * self.c)[0])

        # Remainder
        else:
            slot = int_value % self.size

        return slot

    def insert(self, item):
        """
        Inserts an item in the hash table. When using chaining, returns the
        slot and the node object. When using rehashing/quadratic, returns the
        slot. Returns <None> if could not find an empty slot (only when using
        rehashing/quadratic).

        Notes for the rehashing/quadratic methods:
        - They have been lumped together playing on the value of parameters
          skip and fact (for rehashing: skip > 0, fact = 0; for quadratic:
          skip = 0, fact > 0).
        - Quantities <n_slots> and <n_items> are always equal.
        - They may fail to find an empty slot even if the hash table is not
          full, depending on the values of skip/fact and the table size.
        - An empty slot must be found in at most <size> tentatives, or it will
          never be found.
        - If the table size is a prime number, rehashing will never fail (no
          matter the skip value) to find an empty slot, while quadratic may
          still fail.
        """
        # Convert the item to an integer value
        int_value = self.convert(item)

        # Call the hashing method
        slot = self.hash_index(int_value)

        # If using chaining
        if (self.collision == 'chaining'):

            self.n_items += 1

            # If the slot is empty init the DLL and insert the item
            if (self.table[slot] is None):
                self.table[slot] = DLL([item])
                self.n_slots += 1
                return (slot, self.table[slot].head)

            # If the slot is not empty add the item to the back of the DLL
            else:
                return (slot, self.table[slot].add_back(item))

        # If using rehashing/quadratic
        else:

            # If the slot is empty insert the item
            if (self.table[slot] is None):
                self.table[slot] = item

            # If the slot is not empty
            else:
                i = 0
                slot0 = slot

                while (self.table[slot] is not None):
                    i += 1
                    if (i == self.size):        # Could not find an empty slot
                        return None
                    slot = (slot0 + (self.skip + self.fact * i) * i) % self.size

                self.table[slot] = item         # Found an empty slot

            self.n_slots += 1
            self.n_items += 1

            return slot

    def delete(self, item):
        """
        Deletes an item from the hash table and returns <True>. Returns <False>
        if the item is not found.
        """
        # If using chaining
        if (self.collision == 'chaining'):

            # Search for the item
            slot, node = self.search(item)

            # If the item is not found
            if (node is None):
                return False

            # If the item is found
            else:
                self.table[slot].remove(node)

                # Delete the list from the table if no items left
                if (self.table[slot].size == 0):
                    self.table[slot] = None
                    self.n_slots -= 1

        # If using rehashing/quadratic
        else:

            # Search for the item
            slot = self.search(item)

            # If the item is not found
            if (slot is None):
                return False

            # If the item is found
            else:
                self.table[slot] = None
                self.state[slot] = True
                self.n_slots -= 1

        self.n_items -= 1

        return True

    def search(self, item):
        """
        Searches an item in the hash table. When using chaining, returns the
        slot and the node object. When using rehashing/quadratic, returns the
        slot. In all cases returns <None> if the item is not found.
        """
        # Convert the item to an integer value
        int_value = self.convert(item)

        # Call the hashing method
        slot = self.hash_index(int_value)

        # If using chaining
        if (self.collision == 'chaining'):

            # If the slot is empty
            if (self.table[slot] is None):
                return (slot, None)

            # If the slot is not empty
            else:
                return (slot, self.table[slot].search(item))

        # If using rehashing/quadratic
        else:

            # If the slot is empty
            if (self.table[slot] is None):
                return None

            # If the slot is not empty
            else:
                i = 0
                new_slot = slot

                # Check all occupied/deleted slots
                while ((self.table[new_slot] is not None) or
                       (self.state[new_slot] is True)):

                    if (self.table[new_slot] == item):      # Found the item
                        return new_slot
                    i += 1
                    if (i == self.size):        # Could not find the item
                        return None
                    new_slot = (slot + (self.skip + self.fact * i) * i) \
                                % self.size

                # Found and empty and never deleted slot
                return None

    def clear(self):
        """
        Remove all items from the hash table.
        """
        self.table = [None] * self.size
        self.state = [False] * self.size
        self.n_slots = 0
        self.n_items = 0


if __name__ == '__main__':
    """
    Test the HashTable class and the prime number functions.
    """
    print('\n\n------- Examples with prime numbers -------')

    print('\n==== Check if 15 is prime:')
    print('- deterministic method:', is_prime_det(15))              # False
    print('- probabilistic method:', is_prime_prob(15, k=3))        # False

    print('\n==== Find the first prime number higher than 15:')
    print('- deterministic method:', find_prime(15))                        # 17
    print('- probabilistic method:', find_prime(15, method='prob', k=3))    # 17

    print('\n\n------- Examples using "remainder" and "chaining" -------')

    print('\n==== Create a hash table with size of 17 and add items:')
    ht = HashTable(17, init_list=[320, (6.4, 3.3), 's', True, 'hello', -10.2],
                   hashing='remainder', collision='chaining')
    ht.insert(77)
    ht.insert(-997)
    ht.insert('hello world')
    ht.insert(False)
    ht.insert(25.453)

    # (1, [(6.4, 3.3)])
    # (2, ['hello', 25.453])
    # (4, ['hello world'])
    # (6, [320, -997, False])
    # (7, [-10.2])
    # (12, [77])
    # (13, ['s', True])
    items = ht.items()
    for item in items:
        print(item)

    # HashTable object
    # - total size = 17
    # - occupied slots = 7
    # - number of items = 11
    # - load factor = 0.412
    # - hashing method = remainder
    # - collision method = chaining
    print(ht)

    print('\n==== Examples with search:')
    print(ht.search(77))                # (12, DLnode object with data = 77)
    print(ht.search(25.453))            # (2, DLnode object with data = 25.453)
    print(ht.search(False))             # (6, DLnode object with data = False)
    print(ht.search('not here'))        # (4, None)

    print('\n==== Examples with delete:')
    print(ht.delete(-10.2))             # True
    print(ht.delete(25.453))            # True
    print(ht.delete(-997))              # True
    print(ht.delete('s'))               # True
    print(ht.delete('not here'))        # False

    print('\n==== Resulting table and stats after delete:')
    # (1, [(6.4, 3.3)])
    # (2, ['hello'])
    # (4, ['hello world'])
    # (6, [320, False])
    # (12, [77])
    # (13, [True])
    items = ht.items()
    for item in items:
        print(item)

    # HashTable object
    # - total size = 17
    # - occupied slots = 6
    # - number of items = 7
    # - load factor = 0.353
    # - hashing method = remainder
    # - collision method = chaining
    print(ht)

    print('\n\n------- Examples using "folding" and "rehashing" -------')

    print('\n==== Create a hash table with size of 17 and add items:')
    ht = HashTable(17, init_list=[320, (6.4, 3.3), 's', True, 'hello', -10.2],
                   hashing='folding', collision='rehashing', digit=2, param=3)
    ht.insert(77)
    ht.insert(-997)
    ht.insert('hello world')
    ht.insert(False)
    ht.insert(25.453)

    # (0, 320)
    # (1, 'hello world')
    # (2, 'hello')
    # (3, False)
    # (4, 77)
    # (5, -10.2)
    # (7, -997)
    # (8, (6.4, 3.3))
    # (9, True)
    # (15, 25.453)
    # (16, 's')
    items = ht.items()
    for item in items:
        print(item)

    # HashTable object
    # - total size = 17
    # - occupied slots = 11
    # - number of items = 11
    # - load factor = 0.647
    # - hashing method = folding
    # - collision method = rehashing
    print(ht)

    print('\n==== Examples with search:')
    print(ht.search(77))                # 4
    print(ht.search(25.453))            # 15
    print(ht.search(False))             # 3
    print(ht.search('not here'))        # None

    print('\n==== Examples with delete:')
    print(ht.delete(-10.2))             # True
    print(ht.delete(25.453))            # True
    print(ht.delete(-997))              # True
    print(ht.delete('s'))               # True
    print(ht.delete('not here'))        # False

    print('\n==== Resulting table and stats after delete:')
    # (0, 320)
    # (1, 'hello world')
    # (2, 'hello')
    # (3, False)
    # (4, 77)
    # (8, (6.4, 3.3))
    # (9, True)
    items = ht.items()
    for item in items:
        print(item)

    # HashTable object
    # - total size = 17
    # - occupied slots = 7
    # - number of items = 7
    # - load factor = 0.412
    # - hashing method = folding
    # - collision method = rehashing
    print(ht)

    print('\n==== Examples with convert:')
    print(ht.convert(-10.2))             # 721
    print(ht.convert(25.453))            # 1073
    print(ht.convert(-997))              # 550
    print(ht.convert('s'))               # 115
